"""Lint: SKILL.md files must stay under a length budget.

Rationale (v4.0): Prior versions had 329-547 line SKILL.md files where
critical IRON RULES were buried. v4.0 caps SKILL.md at 250 lines so the
most important content fits on a couple of screens.

References go in references/, agents go in agents/, examples go in
examples/. SKILL.md is the table-of-contents and contract.

Legacy v3.3 skills live under archive/v3/ and are not iterated.
"""
from __future__ import annotations

import sys
from pathlib import Path

from _skill_lint import iter_skill_files

DEFAULT_LIMIT = 250
META_SKILLS = frozenset({"ai-research-pipeline"})
META_LIMIT = 250


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    failures: list[tuple[Path, int, int]] = []

    for skill_md in iter_skill_files(root):
        skill_name = skill_md.parent.name
        limit = META_LIMIT if skill_name in META_SKILLS else DEFAULT_LIMIT
        line_count = sum(1 for _ in skill_md.open(encoding="utf-8"))
        if line_count > limit:
            failures.append((skill_md, line_count, limit))

    if failures:
        print("FAIL: SKILL.md length budget exceeded:")
        for path, n, limit in failures:
            rel = path.relative_to(root)
            print(f"  {rel}: {n} lines > {limit} (over by {n - limit})")
        print()
        print("Fix: move long sections to references/ or agents/ subdirectories.")
        return 1

    print(f"PASS: All SKILL.md files within length budget ({DEFAULT_LIMIT}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
