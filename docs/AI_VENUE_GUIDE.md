# AI Venue Guide

What you need to know about each major AI/ML venue. Used by ai-research-skills as venue-aware defaults; use this guide directly when planning a submission.

> All values cross-reference [`shared/venue_db/<venue>.yaml`](../shared/venue_db/) which is the machine-readable source of truth. This guide is the human-readable companion.

---

## NeurIPS — Conference on Neural Information Processing Systems

| Aspect | Value |
|---|---|
| Deadline | Late May (abstract mid-May) |
| Page limit | 9 main + unlimited refs/appendix |
| Reviewers | 4 |
| Score scale | 1-10 (overall) + soundness/presentation/contribution 1-4 |
| Rebuttal | Single round, ≈6000 words total |
| Disclosure | Required (LLM beyond polishing) |
| Reproducibility | NeurIPS Paper Checklist mandatory |
| Broader Impact | Recommended, often expected |
| Tone | Formal; reviewers heavy-loaded |

**Key tactics**: 
- Strong abstract opening (4 reviewers each spend ≤5 min on first scan)
- Limitations section is a separate Paper Checklist item — don't skip
- Anonymous supplementary material allowed and expected
- Code release recommended; provide anonymized link

---

## ICLR — International Conference on Learning Representations

| Aspect | Value |
|---|---|
| Deadline | Early October (abstract late Sept) |
| Page limit | 10 main + unlimited refs/appendix |
| Reviewers | 3 |
| Score scale | 1-10 (overall) + soundness/presentation/contribution 1-4 |
| Rebuttal | Multi-round OpenReview discussion |
| Disclosure | Required |
| Reproducibility | Reproducibility Statement mandatory; code at submission expected |
| Broader Impact | Optional |
| Tone | OpenReview public discussion — engagement matters |

**Key tactics**:
- Multi-round rebuttal is uniquely high-leverage; first response is critical
- Reviewers actively check arxiv submission dates for "concurrent work" claims
- Long appendix (50+ pages) is normal
- Engaging with reviewer comments materially affects scores

---

## ICML — International Conference on Machine Learning

| Aspect | Value |
|---|---|
| Deadline | Early February (abstract late Jan) |
| Page limit | 8 main + unlimited refs/appendix |
| Reviewers | 3 |
| Score scale | 1-10 |
| Rebuttal | Single round, ≈5000 words |
| Disclosure | Required |
| Reproducibility | Recommended (not yet mandatory checklist) |
| Broader Impact | Recommended |
| Tone | Stricter on theory than NeurIPS/ICLR |

**Key tactics**:
- 8-page limit is tighter than NeurIPS/ICLR — write tighter
- If you build on a theorem, cite rigorously
- Single rebuttal round; make it count

---

## ACL / EMNLP — NLP venues

| Aspect | Value |
|---|---|
| Deadline | ACL: late Feb; EMNLP: late June |
| Page limit | 8 main + unlimited refs/appendix |
| Reviewers | 3 |
| Score scale | 1-5 (excitement, soundness, etc.); 1-5 overall |
| Rebuttal | 1500 words across all reviewers (very tight) |
| Disclosure | **Required in Limitations section** |
| Reproducibility | Responsible NLP Research Checklist mandatory |
| Broader Impact / Ethics | **Mandatory Ethics Statement** |
| Tone | Compact; bullet points acceptable in rebuttal |

**Key tactics**:
- Limitations and Ethics Statement are mandatory sections — not optional
- Rebuttal is uniquely short — bullet ruthlessly
- ARR (ACL Rolling Review) submission flow available
- Same template for ACL + EMNLP (acl-style-files)

---

## CVPR — IEEE/CVF Conference on Computer Vision and Pattern Recognition

| Aspect | Value |
|---|---|
| Deadline | Mid-November (abstract early Nov) |
| Page limit | 8 main + unlimited refs/appendix |
| Reviewers | 3 |
| Score scale | 1-5 |
| Rebuttal | **1 PDF page** (figures allowed!) |
| Disclosure | Required (IEEE policy) |
| Reproducibility | No mandatory checklist; code release expected for SOTA |
| Broader Impact | Optional |
| Tone | Visual; aggressive use of figures |

**Key tactics**:
- 1-page rebuttal PDF is uniquely tight — use figures in rebuttal
- High submission volume (~10K) → reviewer fatigue
- Compare to all major baselines or expect criticism

---

## AAAI — AAAI Conference on Artificial Intelligence

| Aspect | Value |
|---|---|
| Deadline | Mid-August (abstract early Aug) |
| Page limit | 7 main + 2 refs + unlimited appendix |
| Reviewers | 3 |
| Score scale | 1-10 |
| Rebuttal | ≈4500 words |
| Disclosure | Required |
| Reproducibility | AAAI Reproducibility Checklist mandatory |
| Broader Impact | Recommended |
| Tone | Broader AI community (includes symbolic AI, planning) |

**Key tactics**:
- 2-page reference cap forces hard prioritization
- Two-phase review (abstract + full paper)
- Broader sub-field range than NeurIPS/ICLR

---

## arXiv — Preprint Server

| Aspect | Value |
|---|---|
| Deadline | Rolling |
| Page limit | None |
| Review | None |
| Disclosure | Optional but recommended |
| Reproducibility | Author discretion |

**Key tactics**:
- Use as pre-conference move (post AFTER acceptance to build citation momentum)
- Categories: cs.LG, cs.CL, cs.CV, cs.AI, stat.ML
- arXiv is increasingly checked during peer review for "concurrent work" claims

---

## Cheat Sheet: Picking a Venue

| Goal | Venue |
|---|---|
| ML method, generalist | NeurIPS, ICML, ICLR |
| Deep learning emphasis | ICLR > NeurIPS > ICML |
| Theory emphasis | ICML > NeurIPS |
| NLP | ACL or EMNLP |
| Vision | CVPR, ICCV, ECCV |
| Multimodal | NeurIPS, CVPR, or domain-specific |
| Broader AI (incl. symbolic) | AAAI, IJCAI |
| Workshop / fast track | NeurIPS workshops, ICLR Tiny Papers |
| Position paper | NeurIPS, ICML (specific tracks) |

## Cross-Venue Considerations

- **Double-blind**: NeurIPS, ICML, ACL, EMNLP, CVPR, AAAI all double-blind
- **OpenReview**: ICLR, NeurIPS (since 2023), some workshops
- **Code release at submission**: ICLR mandatory; others recommended
- **Ethics review**: NeurIPS opt-in; ACL/EMNLP mandatory

---

## When venue YAML is missing

If you're submitting to a venue not in `shared/venue_db/`:

1. Use `arxiv` as a starting placeholder
2. Add a YAML for the new venue (see `shared/venue_db/README.md` schema)
3. PR back to the repo
