import unittest
from pathlib import Path

from motpt.diagnostics.schema import FailureCaseRef
from motpt.evaluation.protocol import EvaluationIdentity
from scripts.validate_repository import ROOT, validate


class TestScaffold(unittest.TestCase):
    def test_governance_bootstrap_hold(self):
        self.assertEqual(validate(ROOT), [])

    def test_case_schema_observation_not_causation(self):
        case = FailureCaseRef(
            dataset="SyntheticMOT", split="val", sequence="s1",
            first_frame=1, last_frame=3, kind="IDSW",
            baseline_commit="synthetic-only", output_sha256="hash",
        )
        self.assertEqual(case.evidence_level, "OBSERVED")
        with self.assertRaises(ValueError):
            FailureCaseRef("s", "val", "s", 3, 1, "IDSW", "commit", "hash")

    def test_evaluator_schema_does_not_run_evaluation(self):
        identity = EvaluationIdentity(
            "SyntheticMOT", "val", "commit", "TrackEval", "test-v1", "synthetic",
        )
        self.assertEqual(identity.split, "val")


if __name__ == "__main__":
    unittest.main()
