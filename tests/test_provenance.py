import hashlib
import tempfile
import unittest
from pathlib import Path

from motpt.config.provenance import canonical_json, config_sha256, sha256_file


class TestProvenance(unittest.TestCase):
    def test_order_independent(self):
        self.assertEqual(config_sha256({"b": 2, "a": 1}), config_sha256({"a": 1, "b": 2}))
        self.assertEqual(canonical_json({"z": 1, "a": 2}), '{"a":2,"z":1}')

    def test_nan_rejected(self):
        with self.assertRaises(ValueError):
            config_sha256({"bad": float("nan")})

    def test_file_hash(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "synthetic.bin"
            path.write_bytes(b"motpt")
            self.assertEqual(sha256_file(path), hashlib.sha256(b"motpt").hexdigest())


if __name__ == "__main__":
    unittest.main()
