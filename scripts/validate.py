#!/usr/bin/env python3
"""Validate skills/*/SKILL.md against the Agent Skills spec and check repo links.

Standard library only. Exit code 1 on any failure.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors = []


def fail(msg):
    errors.append(msg)


def parse_frontmatter(text, path):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        fail(f"{path}: missing YAML frontmatter")
        return {}
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


def check_links(md_path):
    text = md_path.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    for link in re.findall(r"\]\(([^)\s]+)\)", text):
        if re.match(r"^(https?:|mailto:|#)", link):
            continue
        target = (md_path.parent / link.split("#")[0]).resolve()
        if not target.exists():
            fail(f"{md_path.relative_to(ROOT)}: broken link -> {link}")


skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
if not skills:
    fail("no skills/*/SKILL.md found")

for skill in skills:
    rel = skill.relative_to(ROOT)
    text = skill.read_text(encoding="utf-8")
    fm = parse_frontmatter(text, rel)
    name = fm.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        fail(f"{rel}: invalid name {name!r}")
    if name != skill.parent.name:
        fail(f"{rel}: name {name!r} must match directory {skill.parent.name!r}")
    desc = fm.get("description", "")
    if not desc or len(desc) > 1024:
        fail(f"{rel}: description must be 1-1024 chars (got {len(desc)})")
    if len(fm.get("compatibility", "")) > 500:
        fail(f"{rel}: compatibility over 500 chars")
    if "metadata" in fm and not isinstance(fm["metadata"], dict):
        fail(f"{rel}: metadata must be a mapping")
    if len(text.splitlines()) > 500:
        fail(f"{rel}: SKILL.md over 500 lines; move detail to references/")
    check_links(skill)
    for ref in skill.parent.rglob("*.md"):
        check_links(ref)

for md in sorted(ROOT.glob("*.md")) + sorted((ROOT / "examples").glob("*.md")):
    check_links(md)

readmes = sorted(ROOT.glob("README*.md"))
langs = [p.name for p in readmes]
for readme in readmes:
    body = readme.read_text(encoding="utf-8")
    for other in langs:
        if other not in body:
            fail(f"{readme.name}: missing language link to {other}")

secret = re.compile(r"(ghp_[A-Za-z0-9]{20,}|github_pat_|sk-[A-Za-z0-9]{20,}|BEGIN [A-Z ]*PRIVATE KEY|/var/minis|minis://)")
for f in ROOT.rglob("*"):
    if f.is_file() and ".git" not in f.parts and f.suffix in {".md", ".html", ".py", ".yml", ".yaml"}:
        if f.name == "validate.py":
            continue
        if secret.search(f.read_text(encoding="utf-8", errors="ignore")):
            fail(f"{f.relative_to(ROOT)}: possible secret or local-only path")

if errors:
    print("\n".join(f"FAIL {e}" for e in errors))
    sys.exit(1)
print(f"OK: {len(skills)} skill(s), {len(readmes)} README(s) validated")
