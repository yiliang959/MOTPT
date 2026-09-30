"""Small strict parser for MOT text rows; no filesystem paths are hard-coded.

Parses raw MOT-format text only. GT scoring/filtering is benchmark-specific and
must be implemented under a later frozen evaluation contract.
"""
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from math import isfinite
from typing import Iterator


@dataclass(frozen=True)
class MOTRow:
    frame: int
    object_id: int
    x: float
    y: float
    w: float
    h: float
    confidence: float | None
    columns: tuple[str, ...]

    @property
    def xywh(self) -> tuple[float, float, float, float]:
        return (self.x, self.y, self.w, self.h)


def parse_mot_line(line: str) -> MOTRow:
    """Read one MOT CSV line; keep extra fields and original column values."""
    parts = tuple(cell.strip() for cell in next(csv.reader([line])))
    if len(parts) < 6:
        raise ValueError("MOT row needs at least frame,id,x,y,w,h")
    try:
        frame, object_id = int(parts[0]), int(parts[1])
        x, y, w, h = (float(value) for value in parts[2:6])
        conf = float(parts[6]) if len(parts) >= 7 and parts[6] else None
    except (ValueError, OverflowError) as exc:
        raise ValueError("Invalid numeric field in MOT row") from exc
    values = (x, y, w, h) + (() if conf is None else (conf,))
    if frame < 1 or any(not isfinite(value) for value in values) or w < 0 or h < 0:
        raise ValueError("Invalid frame, non-finite value, or negative box extent")
    return MOTRow(frame, object_id, x, y, w, h, conf, parts)


def read_mot_rows(path: str | Path) -> Iterator[MOTRow]:
    """Yield rows without interpreting GT classes, confidence or IDs."""
    with Path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        for lineno, raw in enumerate(handle, start=1):
            stripped = raw.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                yield parse_mot_line(stripped)
            except ValueError as exc:
                raise ValueError(f"{path}:{lineno}: {exc}") from exc
