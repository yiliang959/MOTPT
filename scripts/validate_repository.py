"""Pure CPU repository checks. Does not inspect user datasets or run models."""
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

    execution = gov.get("execution", {})
    if execution.get("state") != "HOLD__G0_DISCUSSION_ONLY__NO_SCIENTIFIC_EXECUTION":
        errors.append("G0_DISCUSSION_MUST_REMAIN_EXECUTION_HOLD")

    blocked = set(execution.get("denied_until_separately_released", []))
    mandatory = {
        "DATASET_CONSUMING_ANALYSIS", "NATIVE_MODEL_FORWARD", "GPU_MODEL_FORWARD",
        "OPTIMIZER_STEP", "TRAINING", "ONLINE_VAL_INFERENCE",
        "OFFICIAL_VAL_TRACKEVAL", "OFFICIAL_TEST", "MODEL_ARCHITECTURE_IMPLEMENTATION",
    }
    if not mandatory <= blocked:
        errors.append("MISSING_EXECUTION_DENIAL")

    science = gov.get("science", {})
    if science.get("research_hypothesis") != "PERSISTENT_OBJECT_SPECIFIC_LATENT_FLOW_BELIEF__WORKING_V0":
        errors.append("WORKING_RESEARCH_HYPOTHESIS_MISMATCH")
    if science.get("scientific_contract") != "V0_CONCEPT_OWNER_ACCEPTED__NOT_G0_FROZEN":
        errors.append("SCIENTIFIC_CONTRACT_STATUS_MISMATCH")
    if science.get("accepted_model") != "NONE":
        errors.append("UNAUTHORIZED_ACCEPTED_MODEL")
    if science.get("observation_horizon") != "NO_FIXED_OBSERVATION_WINDOW__PERSISTENT_RECURSIVE_BELIEF":
        errors.append("OBSERVATION_HORIZON_CONTRACT_MISMATCH")

    workflow = gov.get("workflow", {})
    if workflow.get("current_active_research_issue") != 1:
        errors.append("ACTIVE_RESEARCH_ISSUE_MISMATCH")
    if workflow.get("current_active_research_branch") != "research/1-motpt-v0-formulation":
        errors.append("ACTIVE_RESEARCH_BRANCH_MISMATCH")

    if not gov.get("cross_repository", {}).get("private_to_public_review_required"):
        errors.append("MISSING_PRIVATE_TO_PUBLIC_REVIEW")

    current = root / "docs/CURRENT.md"
    if current.is_file():
        current_text = current.read_text(encoding="utf-8")
        if "EXECUTION_STATE = HOLD__G0_DISCUSSION_ONLY__NO_SCIENTIFIC_EXECUTION" not in current_text:
            errors.append("CURRENT_NOT_G0_DISCUSSION_HOLD")
        if "ACTIVE_RESEARCH_ISSUE = #1" not in current_text:
            errors.append("CURRENT_RESEARCH_ISSUE_MISMATCH")

    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for issue in problems:
            print(f"FAIL: {issue}")
        raise SystemExit(1)
    print("MOTPT_G0_DISCUSSION_STATIC_CHECK = PASS")
