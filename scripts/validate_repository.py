"""Bootstrap-only, pure CPU repository checks. Does not inspect user datasets."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "README.md", "AGENTS.md", "CLAUDE.md", "governance.json",
    "docs/RESEARCH.md", "docs/EVIDENCE.md", "docs/CURRENT.md",
    "docs/BASELINE.md", "docs/DIAGNOSTICS.md", "docs/CROSS_REPO_REUSE.md",
    "motpt/__init__.py", "motpt/config/provenance.py", "motpt/data/mot_io.py",
    "motpt/diagnostics/schema.py", "motpt/evaluation/protocol.py",
    ".github/workflows/quality.yml",
)


def validate(root: Path = ROOT) -> list[str]:
    errors = [f"MISSING:{path}" for path in REQUIRED if not (root / path).is_file()]
    path = root / "governance.json"
    if not path.is_file():
        return errors
    try:
        gov = json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        return errors + [f"INVALID_GOVERNANCE_JSON:{exc}"]
    if gov.get("project_id") != "MOTPT" or gov.get("repository") != "yiliang959/MOTPT":
        errors.append("WRONG_REPOSITORY_AUTHORITY")
    if gov.get("repository_visibility") != "PUBLIC":
        errors.append("PUBLIC_VISIBILITY_BOUNDARY_MISSING")
    if not gov.get("execution", {}).get("state", "").startswith("HOLD__BOOTSTRAP_ONLY"):
        errors.append("BOOTSTRAP_MUST_REMAIN_HOLD")
    blocked = set(gov.get("execution", {}).get("denied_until_separately_released", []))
    mandatory = {"GPU_MODEL_FORWARD", "OPTIMIZER_STEP", "OFFICIAL_TEST", "ONLINE_VAL_INFERENCE"}
    if not mandatory <= blocked:
        errors.append("MISSING_EXECUTION_DENIAL")
    science = gov.get("science", {})
    if science.get("research_hypothesis") != "UNDEFINED__OWNER_DISCUSSION_PENDING":
        errors.append("SCIENTIFIC_HYPOTHESIS_PREMATURELY_FROZEN")
    if science.get("accepted_model") != "NONE":
        errors.append("UNAUTHORIZED_ACCEPTED_MODEL")
    if not gov.get("cross_repository", {}).get("private_to_public_review_required"):
        errors.append("MISSING_PRIVATE_TO_PUBLIC_REVIEW")
    current = (root / "docs/CURRENT.md")
    if current.is_file() and "EXECUTION_STATE = HOLD__BOOTSTRAP_ONLY" not in current.read_text(encoding="utf-8"):
        errors.append("CURRENT_NOT_BOOTSTRAP_HOLD")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for issue in problems:
            print(f"FAIL: {issue}")
        raise SystemExit(1)
    print("MOTPT_BOOTSTRAP_STATIC_CHECK = PASS")
