"""Lint: SKILL.md files must stay under a length budget.

Rationale (v4.0): Prior versions had 329-547 line SKILL.md files where
critical IRON RULES were buried. v4.0 caps SKILL.md at 250 lines so the
most important content fits on a couple of screens.

References go in references/, agents go in agents/, examples go in
examples/. SKILL.md is the table-of-contents and contract.
"""
from __future__ import annotations

import sys
from pathlib import Path

from _skill_lint import iter_skill_files

# v4.0 atomic skills target ≤200; meta-skills (research-pipeline) get a small bump.
DEFAULT_LIMIT = 250
META_SKILLS = frozenset({"research-pipeline"})
META_LIMIT = 250

# v3.3 legacy skills are exempt during 6-month migration window.
LEGACY_SKILLS = frozenset(
    {"deep-research", "academic-paper", "academic-paper-reviewer", "academic-pipeline"}
)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    failures: list[tuple[Path, int, int]] = []
    legacy_warnings: list[tuple[Path, int]] = []

    for skill_md in iter_skill_files(root):
        skill_name = skill_md.parent.name
        if skill_name in LEGACY_SKILLS:
            line_count = sum(1 for _ in skill_md.open(encoding="utf-8"))
            legacy_warnings.append((skill_md, line_count))
            continue

        limit = META_LIMIT if skill_name in META_SKILLS else DEFAULT_LIMIT
        line_count = sum(1 for _ in skill_md.open(encoding="utf-8"))
        if line_count > limit:
            failures.append((skill_md, line_count, limit))

    if legacy_warnings:
        print("WARNING (legacy v3.3 skills exempt during migration):")
        for path, n in legacy_warnings:
            rel = path.relative_to(root)
            print(f"  {rel}: {n} lines (legacy; will be removed by 2026-10)")
        print()

    if failures:
        print("FAIL: SKILL.md length budget exceeded:")
        for path, n, limit in failures:
            rel = path.relative_to(root)
            print(f"  {rel}: {n} lines > {limit} (over by {n - limit})")
        print()
        print("Fix: move long sections to references/ or agents/ subdirectories.")
        return 1

    print(f"PASS: All non-legacy SKILL.md files within length budget ({DEFAULT_LIMIT}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
