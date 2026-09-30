"""Immutable evaluator identity metadata, with NO scorer execution.

Reading/constructing this object does not authorize VAL or official TEST.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvaluationIdentity:
    dataset: str
    split: str
    baseline_commit: str
    evaluator_name: str
    evaluator_version: str
    scored_population: str

    def __post_init__(self) -> None:
        if self.split not in {"train", "val", "test"}:
            raise ValueError("Explicit dataset split is required")
        if any(not value for value in (
            self.dataset, self.baseline_commit, self.evaluator_name,
            self.evaluator_version, self.scored_population,
        )):
            raise ValueError("Missing evaluation identity field")
