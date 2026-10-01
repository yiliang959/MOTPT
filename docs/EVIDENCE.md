# MOTPT — Scientific Evidence Ledger

```text
STATUS = EMPTY__NO_ACCEPTED_MOTPT_SCIENTIFIC_RESULTS
CANONICAL_EVIDENCE_FILE = docs/EVIDENCE.md
UPDATE_POLICY = IN_PLACE_ONLY
PER_RUN_EVIDENCE_MD = FORBIDDEN
RAW_ARTIFACTS_IN_GIT = FORBIDDEN
BASELINE_PARITY = NOT_YET_EXECUTED
EXTERNAL_PROJECT_EVIDENCE = REFERENCE_ONLY__NOT_AUTOMATICALLY_ACCEPTED
```

## 1. Role of this file

This is the **single canonical scientific evidence ledger** for MOTPT.

All accepted, pending, negative, falsifying or superseded scientific findings that materially affect the research direction belong here. Do not create a new evidence Markdown file for each run, issue, gate, model version, epoch or dataset.

Git keeps the historical versions of this ledger. This file keeps the **current scientific interpretation**.

## 2. Evidence is not raw output

Raw logs, checkpoints, videos, prediction dumps, large JSON/CSV tables and run directories stay outside Git.

An evidence entry references them by immutable identity when needed:

- source/code commit SHA;
- experiment ID;
- checkpoint/config SHA-256;
- input artifact SHA-256;
- dataset + official split + exact population/denominator;
- evaluator + protocol;
- result/artifact hash, manifest ID or stable external path;
- control/parity result.

Do not copy raw output into a new Markdown file just to preserve it.

## 3. Evidence states

Use one of:

- `PENDING_REVIEW` — produced under an authorized contract but not scientifically adjudicated;
- `ACCEPTED` — reviewed and allowed to support the current scientific conclusion;
- `NEGATIVE` — valid evidence against a hypothesis/module/claim;
- `FALSIFYING` — evidence that invalidates a frozen assumption and requires contract revision;
- `SUPERSEDED` — valid historical evidence whose interpretation/population was replaced; keep only the minimal current note and provenance;
- `REFERENCE_ONLY` — external or cross-project evidence that has not been reproduced/accepted for MOTPT.

## 4. Entry format

Add/update entries in place using this structure:

```markdown
### E### — <short scientific question>

- Status:
- Contract / gate:
- Source commit:
- Dataset / split / population:
- Config / checkpoint / input hashes:
- Evaluator / protocol:
- Artifact reference / hash:
- Controls / parity:
- Result:
- Scientific interpretation:
- Limitations:
- Supersedes / superseded by:
```

One evidence entry represents a **scientific question or adjudicated comparison**, not every execution attempt.

Repeated runs that answer the same question should update the same entry or be summarized into one comparison table.

## 5. Accepted evidence

None yet.

## 6. Pending evidence

None yet.

## 7. Negative / falsifying evidence

None yet.

## 8. Reference-only evidence

### R001 — TCR-MOT and other external project observations

- Status: `REFERENCE_ONLY`
- Rule: TCR-MOT findings, literature results and other external evidence may motivate MOTPT hypotheses but are not automatically accepted MOTPT scientific evidence.
- Requirement: reproduce or independently validate under a frozen MOTPT contract before promotion to `ACCEPTED`.

## 9. Anti-proliferation rule

Do not create:

```text
docs/EVIDENCE_v2.md
docs/EVIDENCE_final.md
docs/EVIDENCE_<issue>.md
docs/evidence_<run>.md
docs/results/<experiment>/README.md
```

If evidence changes, edit **this file**. Git history is the archive.
