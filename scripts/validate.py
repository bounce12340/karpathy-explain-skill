#!/usr/bin/env python3
"""Validate this repository's Agent Skills and documentation.

Checks:
  1. skills/*/SKILL.md frontmatter follows the Agent Skills spec.
  2. Relative Markdown links resolve.
  3. Every README links to every other README language.
  4. Evidence anchors such as [confirmed scripts/validate.py:12] point to
     a real file and an existing line.
  5. No secrets or local-only paths in tracked text files.

Standard library only. Exit code 1 on any failure.
Usage: python3 scripts/validate.py [repo-root]
"""
import pathlib
import re
import subprocess
import sys

NAME_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
ANCHOR_RE = re.compile(
    r"\[(?:confirmed|已確認|已确认|確認済み|확인됨)\s+([\w./-]+\.[A-Za-z0-9]+):(\d+)(?:-(\d+))?\]"
)
SECRET_RE = re.compile(
    r"(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{20,}"
    r"|BEGIN [A-Z ]*PRIVATE KEY|/var/minis|minis://)"
)
TEXT_SUFFIXES = {".md", ".html", ".py", ".yml", ".yaml", ".json", ".txt"}


def tracked_files(root):
    """Files tracked by git; falls back to a filesystem walk outside git."""
    try:
        out = subprocess.run(
            ["git", "-C", str(root), "ls-files", "-z"],
            check=True, capture_output=True,
        ).stdout.decode("utf-8")
        files = [root / p for p in out.split("\0") if p]
        if files:
            return [f for f in files if f.is_file()]
    except (OSError, subprocess.CalledProcessError):
        pass
    return [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    data, current = {}, None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith("  ") and current == "metadata":
            k, _, v = line.strip().partition(":")
            data.setdefault("metadata", {})[k.strip()] = v.strip().strip('"')
            continue
        k, _, v = line.partition(":")
        current = k.strip()
        data[current] = v.strip().strip('"') if v.strip() else {}
    return data


def strip_code(text):
    """Drop fenced blocks and inline code spans.

    Anchors written in plain text are verified; anchors inside code spans are
    treated as format illustrations (e.g. in templates and READMEs).
    """
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def validate(root):
    root = pathlib.Path(root).resolve()
    errors = []
    files = tracked_files(root)
    rel = lambda p: p.relative_to(root).as_posix()

    skills = sorted(p for p in files if re.fullmatch(r"skills/[^/]+/SKILL\.md", rel(p)))
    if not skills:
        errors.append("no skills/*/SKILL.md found")
    for skill in skills:
        r = rel(skill)
        text = skill.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{r}: missing YAML frontmatter")
            continue
        name = fm.get("name", "")
        if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{r}: invalid name {name!r}")
        elif name != skill.parent.name:
            errors.append(f"{r}: name {name!r} must match directory {skill.parent.name!r}")
        desc = fm.get("description", "")
        if not isinstance(desc, str) or not desc or len(desc) > 1024:
            errors.append(f"{r}: description must be 1-1024 chars")
        if len(str(fm.get("compatibility", ""))) > 500:
            errors.append(f"{r}: compatibility over 500 chars")
        if "metadata" in fm and not isinstance(fm["metadata"], dict):
            errors.append(f"{r}: metadata must be a mapping")
        if len(text.splitlines()) > 500:
            errors.append(f"{r}: SKILL.md over 500 lines; move detail to references/")

    for md in (p for p in files if p.suffix == ".md"):
        body = strip_code(md.read_text(encoding="utf-8"))
        for link in LINK_RE.findall(body):
            if re.match(r"^(https?:|mailto:|#)", link):
                continue
            if not (md.parent / link.split("#")[0]).resolve().exists():
                errors.append(f"{rel(md)}: broken link -> {link}")
        for path, start, end in ANCHOR_RE.findall(body):
            target = root / path
            if not target.is_file():
                errors.append(f"{rel(md)}: evidence anchor to missing file {path}")
                continue
            count = len(target.read_text(encoding="utf-8").splitlines())
            last = int(end or start)
            if int(start) < 1 or last > count or last < int(start):
                errors.append(f"{rel(md)}: evidence anchor {path}:{start}{'-' + end if end else ''} outside 1-{count}")

    readmes = sorted(p.name for p in files if re.fullmatch(r"README(\.[\w-]+)?\.md", rel(p)))
    for name in readmes:
        body = (root / name).read_text(encoding="utf-8")
        for other in readmes:
            if f"]({other})" not in body:
                errors.append(f"{name}: missing language link to {other}")

    for f in files:
        if f.suffix in TEXT_SUFFIXES and rel(f) != "scripts/validate.py" and not rel(f).startswith("tests/"):
            if SECRET_RE.search(f.read_text(encoding="utf-8", errors="ignore")):
                errors.append(f"{rel(f)}: possible secret or local-only path")

    return errors, len(skills), len(readmes)


def main(argv):
    root = argv[1] if len(argv) > 1 else pathlib.Path(__file__).resolve().parent.parent
    errors, n_skills, n_readmes = validate(root)
    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        return 1
    print(f"OK: {n_skills} skill(s), {n_readmes} README(s) validated")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
