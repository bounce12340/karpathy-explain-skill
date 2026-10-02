"""Regression tests for scripts/validate.py. Run: python3 -m unittest discover -s tests"""
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import validate  # noqa: E402

SKILL = """---
name: demo-skill
description: "Demo skill for tests."
license: MIT
metadata:
  version: "1.0.0"
---

# Demo
"""


class ValidateTests(unittest.TestCase):
    def setUp(self):
        self.tmp = pathlib.Path(tempfile.mkdtemp())
        (self.tmp / "skills/demo-skill").mkdir(parents=True)
        (self.tmp / "skills/demo-skill/SKILL.md").write_text(SKILL, encoding="utf-8")
        (self.tmp / "README.md").write_text("[EN](README.md) [JA](README.ja.md)\n", encoding="utf-8")
        (self.tmp / "README.ja.md").write_text("[EN](README.md) [JA](README.ja.md)\n", encoding="utf-8")
        (self.tmp / "code.py").write_text("a = 1\nb = 2\nc = 3\n", encoding="utf-8")
        subprocess.run(["git", "init", "-q", str(self.tmp)], check=True)
        self.commit()

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def commit(self):
        subprocess.run(["git", "-C", str(self.tmp), "add", "-A"], check=True)

    def errors(self):
        self.commit()
        return validate.validate(self.tmp)[0]

    def write(self, path, text):
        p = self.tmp / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def test_valid_repo_passes(self):
        self.assertEqual(self.errors(), [])

    def test_bad_name(self):
        self.write("skills/demo-skill/SKILL.md", SKILL.replace("demo-skill", "Demo_Skill"))
        self.assertTrue(any("invalid name" in e for e in self.errors()))

    def test_name_must_match_directory(self):
        self.write("skills/demo-skill/SKILL.md", SKILL.replace("name: demo-skill", "name: other-skill"))
        self.assertTrue(any("must match directory" in e for e in self.errors()))

    def test_description_too_long(self):
        self.write("skills/demo-skill/SKILL.md", SKILL.replace("Demo skill for tests.", "x" * 1025))
        self.assertTrue(any("description" in e for e in self.errors()))

    def test_broken_link(self):
        self.write("README.md", "[EN](README.md) [JA](README.ja.md) [x](missing.md)\n")
        self.assertTrue(any("broken link" in e for e in self.errors()))

    def test_missing_language_link(self):
        self.write("README.ja.md", "[EN](README.md)\n")
        self.assertTrue(any("missing language link" in e for e in self.errors()))

    def test_evidence_anchor_ok(self):
        self.write("notes.md", "Value set here [confirmed code.py:2] and [已確認 code.py:1-3].\n")
        self.assertEqual(self.errors(), [])

    def test_evidence_anchor_line_out_of_range(self):
        self.write("notes.md", "Wrong line [confirmed code.py:9].\n")
        self.assertTrue(any("outside 1-3" in e for e in self.errors()))

    def test_anchor_in_code_span_is_illustration(self):
        self.write("notes.md", "Format: `[confirmed src/auth.ts:42]`\n")
        self.assertEqual(self.errors(), [])

    def test_evidence_anchor_missing_file(self):
        self.write("notes.md", "Wrong file [confirmed nope.py:1].\n")
        self.assertTrue(any("missing file" in e for e in self.errors()))

    def test_secret_detected(self):
        self.write("leak.md", "token ghp_" + "a" * 30 + "\n")
        self.assertTrue(any("possible secret" in e for e in self.errors()))

    def test_untracked_files_ignored(self):
        p = self.tmp / "scratch.md"
        p.write_text("ghp_" + "b" * 30, encoding="utf-8")
        self.assertEqual(validate.validate(self.tmp)[0], [])

    def test_real_repository_passes(self):
        errors, skills, readmes = validate.validate(REPO)
        self.assertEqual(errors, [])
        self.assertGreaterEqual(skills, 1)
        self.assertEqual(readmes, 5)


if __name__ == "__main__":
    unittest.main()
