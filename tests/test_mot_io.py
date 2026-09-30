import tempfile
import unittest
from pathlib import Path

from motpt.data.mot_io import parse_mot_line, read_mot_rows


class TestMOTIO(unittest.TestCase):
    def test_parse_retains_optional_columns(self):
        row = parse_mot_line("1,-1,4,5,20,11,0.8,1,0.2")
        self.assertEqual((row.frame, row.object_id), (1, -1))
        self.assertEqual(row.xywh, (4.0, 5.0, 20.0, 11.0))
        self.assertEqual(row.confidence, 0.8)
        self.assertEqual(row.columns[7], "1")

    def test_missing_optional_conf(self):
        self.assertIsNone(parse_mot_line("5,7,0,1,2,3").confidence)

    def test_reject_invalid_values(self):
        for value in ("0,1,0,0,2,3", "1,2,NaN,0,2,3", "1,2,0,0,-2,3", "abc,2,0,0,1,1"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_mot_line(value)

    def test_reader_preserves_line_number_in_errors(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "synthetic.txt"
            path.write_text("# comment\n\n1,1,0,0,1,1\n2,2,NaN,0,1,1\n", encoding="utf-8")
            rows = read_mot_rows(path)
            self.assertEqual(next(rows).frame, 1)
            with self.assertRaisesRegex(ValueError, r":4:"):
                next(rows)


if __name__ == "__main__":
    unittest.main()
