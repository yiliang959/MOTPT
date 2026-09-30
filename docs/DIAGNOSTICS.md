# MOTPT — Reusable Diagnostic Contract (pre-experiment)

The common failure-case **observation layer** can be shared conceptually with another MOT project without inheriting its proposed cause or corrective model.

## Suggested case identities

Keep at minimum:
- Source: benchmark, official split, sequence, frame interval, pinned baseline source, checkpoint/config identity, input/output hashes and evaluator.
- Observation: Native ACTIVATE candidate(s), Native FINAL emitted row(s), persistent output tracker ID, internal recyclable `id_label` (explicitly separate), scored GT match if evaluator-only, and original row/box geometry.
- Phenomenon tags (not claims of cause): `FN`, `FP`, `IDSW`, `FRAG`, `CANDIDATE_FINAL_GAP`, `MERGE_OR_CARDINALITY_PRESSURE`, `OTHER`.
- Human-review metadata: interval, visualization path/hash and observation notes, never an implicitly approved scientific mechanism.

`MOTPT` is not importing TCR's accepted causal interpretations, factorial interventions or result numbers. Phenomena are hypotheses for independent analysis unless independently verified under a frozen population.

## Information roles

| Information | Intended role |
|---|---|
| Current-frame image/detection and causal state | Potential model input only after G0 freeze |
| Dataset GT / GT identity mapping | TRAIN supervision or evaluator-only as declared |
| Future reappearance or whole-sequence oracle labels | Offline analysis/evaluator only |
| Native ACTIVATE/FINAL logs | Baseline diagnostic evidence, not intrinsic physical truth |
| TrackEval identity events | Evaluation result, not direct runtime model input |

A high-IoU candidate around a GT does not, by itself, identify an IDSW. Preserve source observation and exact denominator, rather than silently mapping all tracker errors to one mechanism.

The generic typed case reference starts at `motpt/diagnostics/schema.py`. It is a schema, not a current dataset inventory; no failure cases have been measured in MOTPT yet.
