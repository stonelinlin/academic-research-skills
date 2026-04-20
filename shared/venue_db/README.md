# venue_db — AI/ML Conference Knowledge Base

YAML-formatted knowledge base for major AI/ML venues. Consumed by:
- `ai-venue-formatter` (template + page limits + disclosure policy)
- `ai-paper-reviewer` (reviewer expectations + scoring rubric)
- `ai-rebuttal-coach` (response word limits + author response phase rules)
- `ai-idea-forge` (recent accept trends — needs runtime arxiv lookup)

## Schema

Each venue YAML must contain:

```yaml
venue: <short-name>
full_name: <official-name>
type: <conference|journal>
fields: [<list-of-primary-fields>]
deadlines:
  abstract: <month-year-pattern>
  full_paper: <month-year-pattern>
page_limits:
  main_text: <int>
  references: <int|unlimited>
  appendix: <int|unlimited>
  rebuttal: <int>
template:
  latex_class: <name>
  bibtex_style: <name>
  template_url: <url>
  local_template: <path-relative-to-shared/templates/>
review_format:
  num_reviewers: <int>
  scoring_scale: <e.g., "1-10">
  required_sections: [<list>]
  rebuttal_phase: <yes|no>
  rebuttal_word_limit: <int|null>
disclosure:
  ai_use_required: <yes|no|recommended>
  policy_url: <url>
  required_statement_location: <e.g., "acknowledgments">
reproducibility:
  checklist_required: <yes|no>
  checklist_url: <url|null>
  code_release_required: <yes|recommended|no>
broader_impact:
  required: <yes|no|recommended>
  section_name: <e.g., "Broader Impact">
notes: |
  <free-text guidance for users>
```

## Status

This is a v4.0 initial seed. Values reflect publicly documented policies as of 2026-04. Users should verify against the venue's call-for-papers before submission.
