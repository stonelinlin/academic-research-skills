"""Lint: shared/venue_db/*.yaml files must conform to the schema.

Required keys per shared/venue_db/README.md:
  venue, full_name, type, fields, deadlines, page_limits, template,
  review_format, disclosure, reproducibility, broader_impact

This linter validates structure and surfaces obvious omissions.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REQUIRED_TOP = [
    "venue",
    "full_name",
    "type",
    "fields",
    "deadlines",
    "page_limits",
    "template",
    "review_format",
    "disclosure",
    "reproducibility",
    "broader_impact",
]

REQUIRED_DEADLINES = ["abstract", "full_paper"]
REQUIRED_PAGE_LIMITS = ["main_text", "references", "appendix", "rebuttal"]
REQUIRED_TEMPLATE = ["latex_class", "bibtex_style", "template_url"]
REQUIRED_REVIEW = [
    "num_reviewers",
    "scoring_scale",
    "required_sections",
    "rebuttal_phase",
    "rebuttal_word_limit",
]
REQUIRED_DISCLOSURE = ["ai_use_required", "policy_url"]
REQUIRED_REPRO = ["checklist_required", "code_release_required"]
REQUIRED_IMPACT = ["required"]

SCHEMA = {
    "(top)": REQUIRED_TOP,
    "deadlines": REQUIRED_DEADLINES,
    "page_limits": REQUIRED_PAGE_LIMITS,
    "template": REQUIRED_TEMPLATE,
    "review_format": REQUIRED_REVIEW,
    "disclosure": REQUIRED_DISCLOSURE,
    "reproducibility": REQUIRED_REPRO,
    "broader_impact": REQUIRED_IMPACT,
}


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    venue_dir = root / "shared" / "venue_db"
    if not venue_dir.is_dir():
        print(f"FAIL: {venue_dir} does not exist")
        return 1

    failures: list[str] = []
    venues_seen: set[str] = set()

    for yaml_file in sorted(venue_dir.glob("*.yaml")):
        try:
            data = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            failures.append(f"{yaml_file.name}: YAML parse error: {exc}")
            continue
        if not isinstance(data, dict):
            failures.append(f"{yaml_file.name}: top-level must be a mapping")
            continue

        # Check top-level
        missing = [k for k in REQUIRED_TOP if k not in data]
        if missing:
            failures.append(f"{yaml_file.name}: missing top-level keys: {missing}")
            continue

        # File name should match venue field
        venue = data.get("venue")
        if yaml_file.stem != venue:
            failures.append(
                f"{yaml_file.name}: filename stem '{yaml_file.stem}' does not match venue '{venue}'"
            )
        if venue in venues_seen:
            failures.append(f"{yaml_file.name}: duplicate venue '{venue}'")
        venues_seen.add(venue)

        # Check nested
        for nest_key, required in SCHEMA.items():
            if nest_key == "(top)":
                continue
            sub = data.get(nest_key)
            if not isinstance(sub, dict):
                failures.append(f"{yaml_file.name}: '{nest_key}' is not a mapping")
                continue
            missing_nested = [k for k in required if k not in sub]
            if missing_nested:
                failures.append(
                    f"{yaml_file.name}: '{nest_key}' missing keys: {missing_nested}"
                )

    if failures:
        print("FAIL: venue_db lint:")
        for f in failures:
            print(f"  {f}")
        return 1

    print(f"PASS: {len(venues_seen)} venue YAML files conform to schema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
