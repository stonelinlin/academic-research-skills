#!/usr/bin/env python3
"""Spec consistency check (v4.0 rewrite).

v3.3 ran detailed README structure assertions tied to MODE_REGISTRY.
v4.0 collapses that to:
  - All declared atomic skills exist as <skill>/SKILL.md
  - README references each atomic skill
  - CHANGELOG references the current suite version
  - docs/ files referenced by README all exist

Legacy v3.3 skills are exempt (kept until 2026-10).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

ATOMIC_SKILLS = [
    "ai-idea-forge",
    "ai-lit-scout",
    "ai-related-positioning",
    "ai-method-architect",
    "ai-paper-writer",
    "ai-figure-smith",
    "ai-integrity-check",
    "ai-paper-reviewer",
    "ai-rebuttal-coach",
    "ai-venue-formatter",
]
META_SKILLS = ["ai-research-pipeline"]

EXPECTED_DOCS = [
    "docs/COMMAND_INDEX.md",
    "docs/AI_VENUE_GUIDE.md",
    "docs/MIGRATION_v3_to_v4.md",
]

EXPECTED_SHARED = [
    "shared/agents/socratic_mentor.md",
    "shared/agents/devils_advocate.md",
    "shared/agents/state_tracker.md",
    "shared/protocols/anti_sycophancy.md",
    "shared/protocols/integrity_protocol.md",
    "shared/venue_db/README.md",
]

EXPECTED_ZH_CN_SKILLS = [
    "zh-CN/README.md",
    *[f"zh-CN/{s}/SKILL.md" for s in ATOMIC_SKILLS + META_SKILLS],
]

EXPECTED_VENUE_YAMLS = [
    "shared/venue_db/neurips.yaml",
    "shared/venue_db/iclr.yaml",
    "shared/venue_db/icml.yaml",
    "shared/venue_db/acl.yaml",
    "shared/venue_db/emnlp.yaml",
    "shared/venue_db/cvpr.yaml",
    "shared/venue_db/aaai.yaml",
    "shared/venue_db/arxiv.yaml",
]


def fail(msg: str) -> None:
    ERRORS.append(msg)


def check_skill_dirs() -> None:
    for skill in ATOMIC_SKILLS + META_SKILLS:
        skill_md = ROOT / skill / "SKILL.md"
        if not skill_md.is_file():
            fail(f"missing skill: {skill}/SKILL.md")


def check_readme_mentions() -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        fail("README.md missing")
        return
    text = readme.read_text(encoding="utf-8")
    for skill in ATOMIC_SKILLS:
        if f"`{skill}`" not in text and f"[{skill}]" not in text and f"({skill}/" not in text:
            fail(f"README.md does not reference skill: {skill}")
    if not re.search(r"v4\.\d+", text):
        fail("README.md does not declare a v4.x version")


def check_changelog() -> None:
    changelog = ROOT / "CHANGELOG.md"
    if not changelog.is_file():
        fail("CHANGELOG.md missing")
        return
    text = changelog.read_text(encoding="utf-8")
    if "[4.1.1]" not in text and "[4.1.0]" not in text and "[4.0.0]" not in text:
        fail("CHANGELOG.md missing [4.1.1], [4.1.0], or [4.0.0] entry")


def check_docs_exist() -> None:
    for doc in EXPECTED_DOCS:
        if not (ROOT / doc).is_file():
            fail(f"missing doc: {doc}")


def check_zh_cn_skills() -> None:
    for f in EXPECTED_ZH_CN_SKILLS:
        if not (ROOT / f).is_file():
            fail(f"missing zh-CN skill doc: {f}")


def check_shared_exists() -> None:
    for f in EXPECTED_SHARED:
        if not (ROOT / f).is_file():
            fail(f"missing shared file: {f}")
    for f in EXPECTED_VENUE_YAMLS:
        if not (ROOT / f).is_file():
            fail(f"missing venue YAML: {f}")


def main() -> int:
    check_skill_dirs()
    check_readme_mentions()
    check_changelog()
    check_docs_exist()
    check_zh_cn_skills()
    check_shared_exists()

    if ERRORS:
        print("FAIL: spec consistency:")
        for e in ERRORS:
            print(f"  {e}")
        return 1
    print(
        f"PASS: {len(ATOMIC_SKILLS)} atomic skills, {len(META_SKILLS)} meta skills, "
        f"{len(EXPECTED_DOCS)} docs, {len(EXPECTED_ZH_CN_SKILLS)} zh-CN files, "
        f"{len(EXPECTED_VENUE_YAMLS)} venue YAMLs all present and referenced."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
