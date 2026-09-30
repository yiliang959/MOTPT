"""Pure provenance helpers; safe for synthetic CPU tests.

These functions record identities but do not grant dataset/model execution.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping


def sha256_file(path: str | Path) -> str:
    """SHA-256 of the exact bytes; stream instead of loading large files."""
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: Any) -> str:
    """Deterministic JSON; non-finite numbers are rejected."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True, allow_nan=False)


def config_sha256(config: Mapping[str, Any]) -> str:
    """Digest of a fully resolved JSON-compatible mapping."""
    return hashlib.sha256(canonical_json(dict(config)).encode("utf-8")).hexdigest()
