# MOTPT — Baseline Registry (pre-freeze)

## Planned baseline: Native MOTIP

Upstream: https://github.com/MCG-NJU/MOTIP

Candidate upstream pin for comparability with TCR-MOT: `ffc0e905ac196a603027eca8d18fb0dff48c8bcc`.

```text
MOTPT_PIN_STATUS = CANDIDATE__NOT_OWNER_FROZEN
MOTPT_CHECKPOINTS = NONE_IMPORTED
MOTPT_CONFIG_IDENTITY = NOT_FROZEN
MOTPT_NATIVE_PARITY = NOT_EXECUTED
EXPERIMENT_PERMISSION = NONE
```

When an authorized baseline setup is opened, independently bind upstream license/commit, exact dependencies/environment, datasets/official split, config/checkpoint SHA-256, detector threshold and native tracker/evaluation output. Record Native output parity against a reference before reuse of a diagnostic dump. TCR checkpoint locations or prior results are not substitutes for independent MOTPT provenance.

Do not copy pretrained weights or upstream code into this Public repository during pre-G0 work. Prefer a separately managed upstream checkout/environment and record its immutable pin/license/provenance here. Vendoring third-party code into MOTPT would require an explicit Owner-approved structure change plus license review.
