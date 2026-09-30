"""Experiment-independent reference to one observed native tracking case.

A tag is an observed phenomenon, NOT an accepted causal mechanism.
An explicit source/hash is mandatory to avoid orphaned shared screenshots.
"""
from __future__ import annotations

from dataclasses import dataclass

CASE_KINDS = frozenset({
    "FN", "FP", "IDSW", "FRAG", "CANDIDATE_FINAL_GAP",
    "MERGE_OR_CARDINALITY_PRESSURE", "OTHER",
})
EVIDENCE_LEVELS = frozenset({"OBSERVED", "DIAGNOSTIC_ORACLE", "HYPOTHESIS"})


@dataclass(frozen=True)
class FailureCaseRef:
    dataset: str
    split: str
    sequence: str
    first_frame: int
    last_frame: int
    kind: str
    baseline_commit: str
    output_sha256: str
    evidence_level: str = "OBSERVED"

    def __post_init__(self) -> None:
        if not self.dataset or not self.sequence or not self.baseline_commit or not self.output_sha256:
            raise ValueError("Missing mandatory case provenance")
        if self.split not in {"train", "val", "test"}:
            raise ValueError("Split must be explicit and official-name-compatible")
        if self.first_frame < 1 or self.last_frame < self.first_frame:
            raise ValueError("Invalid frame interval")
        if self.kind not in CASE_KINDS or self.evidence_level not in EVIDENCE_LEVELS:
            raise ValueError("Unknown case tag or evidence level")
