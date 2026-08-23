import unittest
from pathlib import Path

from strandcheck import (
    classify_change,
    find_invalid_characters,
    normalize_sequence,
    read_sequence_file,
    read_sequence_input,
    validate_sequence,
)


class TestSequenceValidation(unittest.TestCase):
    def test_missing_file_path_is_not_treated_as_dna(self):
        missing_path = "sequence/does_not_exist.txt"

        with self.assertRaisesRegex(FileNotFoundError, "Sequence file not found"):
            read_sequence_input(missing_path)

    def test_sequence_is_read_from_text_file(self):
        file_path = Path(__file__).parent / "sequence" / "bakersyeast_orignial.txt"
        result = read_sequence_file(file_path)

        print(f"read_sequence_file({str(file_path)!r}) -> {result!r}")
        self.assertTrue(result)
        self.assertTrue(set(result.upper()) <= set("ATCG"))

    def test_file_path_is_used_as_sequence_input(self):
        file_path = Path(__file__).parent / "sequence" / "bakersyeast_orignial.txt"
        result = read_sequence_input(str(file_path))

        print(f"read_sequence_input({str(file_path)!r}) -> {result!r}")
        self.assertEqual(result, read_sequence_file(file_path))

    def test_sequence_is_normalized(self):
        sequence = " atgcctatc "
        result = normalize_sequence(sequence)

        print(f"\nnormalize_sequence({sequence!r}) -> {result!r}")
        self.assertEqual(result, "ATGCCTATC")

    def test_invalid_characters_are_found(self):
        sequence = "ATGXCTA"
        result = find_invalid_characters(sequence)

        print(f"find_invalid_characters({sequence!r}) -> {result}")
        self.assertEqual(result, ["X"])

    def test_valid_sequence_is_normalized(self):
        sequence = " atgcctatc "
        result, errors = validate_sequence(sequence)

        print(f"validate_sequence({sequence!r}) -> sequence={result!r}, errors={errors}")
        self.assertEqual(result, "ATGCCTATC")
        self.assertEqual(errors, [])

    def test_invalid_character_is_reported(self):
        sequence = "ATGXCTA"
        result, errors = validate_sequence(sequence)

        print(f"validate_sequence({sequence!r}) -> sequence={result!r}, errors={errors}")
        self.assertEqual(result, "ATGXCTA")
        self.assertIn("Invalid character(s) found: 'X'", errors)

    def test_incomplete_codon_is_reported(self):
        sequence = "ATGCCTA"
        result, errors = validate_sequence(sequence)

        print(f"validate_sequence({sequence!r}) -> sequence={result!r}, errors={errors}")
        self.assertEqual(result, "ATGCCTA")
        self.assertIn("Sequence length is not divisible by 3", errors)


class TestSampleChanges(unittest.TestCase):
    original = "ATGCCTATC"

    def test_substitution_is_checked_before_length_changes(self):
        sample = "ATTCCTATC"
        result = classify_change(self.original, sample)

        print(f"Checks substitution first: {result}")
        self.assertEqual(result, "substitution")

    def test_no_change(self):
        sample = "ATGCCTATC"
        result = classify_change(self.original, sample)

        print(f"classify_change({self.original!r}, {sample!r}) -> {result}")
        self.assertEqual(result, "no change")

    def test_addition(self):
        sample = "ATGCCTAGTC"
        result = classify_change(self.original, sample)

        print(f"classify_change({self.original!r}, {sample!r}) -> {result}")
        self.assertEqual(result, "addition")

    def test_substitution(self):
        sample = "ATTCCTATC"
        result = classify_change(self.original, sample)

        print(f"classify_change({self.original!r}, {sample!r}) -> {result}")
        self.assertEqual(result, "substitution")

    def test_deletion(self):
        sample = "ATGCTATC"
        result = classify_change(self.original, sample)

        print(f"classify_change({self.original!r}, {sample!r}) -> {result}")
        self.assertEqual(result, "deletion")


if __name__ == "__main__":
    unittest.main()