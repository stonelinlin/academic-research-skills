"""Lint: SKILL.md description fields should declare a finite, non-overlapping trigger set.

Rationale (v4.0): With 10 atomic skills, trigger phrases must not overlap.
If two skills compete for the same phrase, the assistant cannot route reliably.

This linter:
  1. Extracts the "Triggers:" segment from each SKILL.md description.
  2. Counts triggers per skill (target: 3-12 distinct phrases).
  3. Flags phrases that appear in multiple skills' trigger lists.

Legacy v3.3 skills live under archive/v3/ and are not iterated.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

from _skill_lint import iter_skill_files, parse_frontmatter

# Phrases that legitimately appear across skills (e.g. shared concepts) — allowlist.
ALLOWLIST_PHRASES = frozenset(
    {
        # very generic verbs that appear naturally
    }
)

MIN_TRIGGERS = 3
MAX_TRIGGERS = 12

TRIGGER_HEADING = re.compile(r"triggers?:\s*(.+)$", re.IGNORECASE | re.DOTALL)


def extract_triggers(description: str) -> list[str]:
    """Pull comma-separated triggers from the 'Triggers:' tail of description."""
    match = TRIGGER_HEADING.search(description)
    if not match:
        return []
    tail = match.group(1).strip().rstrip(".")
    return [phrase.strip().lower() for phrase in tail.split(",") if phrase.strip()]


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    skill_to_triggers: dict[str, list[str]] = {}
    failures: list[str] = []

    for skill_md in iter_skill_files(root):
        skill_name = skill_md.parent.name
        try:
            fm = parse_frontmatter(skill_md)
        except Exception as exc:
            failures.append(f"{skill_md}: cannot parse frontmatter: {exc}")
            continue
        if not fm:
            failures.append(f"{skill_md}: missing frontmatter")
            continue

        description = fm.get("description", "")
        triggers = extract_triggers(description)

        if not triggers:
            failures.append(f"{skill_md}: no 'Triggers:' segment in description")
            continue
        if len(triggers) < MIN_TRIGGERS:
            failures.append(
                f"{skill_md}: only {len(triggers)} triggers; minimum is {MIN_TRIGGERS}"
            )
        if len(triggers) > MAX_TRIGGERS:
            failures.append(
                f"{skill_md}: {len(triggers)} triggers exceeds maximum {MAX_TRIGGERS}; consolidate"
            )
        skill_to_triggers[skill_name] = triggers

    # Check for overlap across skills
    phrase_to_skills: dict[str, list[str]] = defaultdict(list)
    for skill, triggers in skill_to_triggers.items():
        for phrase in triggers:
            if phrase in ALLOWLIST_PHRASES:
                continue
            phrase_to_skills[phrase].append(skill)

    for phrase, skills in sorted(phrase_to_skills.items()):
        if len(skills) > 1:
            failures.append(
                f"OVERLAP: trigger phrase '{phrase}' appears in multiple skills: {sorted(skills)}"
            )

    if failures:
        print("FAIL: trigger word lint:")
        for f in failures:
            print(f"  {f}")
        return 1

    print(f"PASS: {len(skill_to_triggers)} skills with non-overlapping trigger sets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
