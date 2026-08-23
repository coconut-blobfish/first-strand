from pathlib import Path


# These are the only four letters that are valid in a DNA sequence.
VALID_BASES = set("ATCG")


# Clean user input so lowercase letters and extra spaces do not cause problems.
def normalize_sequence(sequence):
	"""Remove surrounding whitespace and use uppercase DNA letters."""
	return sequence.strip().upper()


# Read a sequence saved in a text file. Each line is joined so wrapped sequences
# downloaded from the internet can still be checked as one continuous sequence.
def read_sequence_file(file_path):
	with open(file_path, encoding="utf-8") as sequence_file:
		return "".join(line.strip() for line in sequence_file)


# Treat an existing path as a file; otherwise treat the input as a typed sequence.
def read_sequence_input(value):
	path = Path(value).expanduser()
	if path.is_file():
		return read_sequence_file(path)
	if path.suffix.lower() == ".txt" or "/" in value or "\\" in value:
		raise FileNotFoundError(f"Sequence file not found: {value}")
	return value


# Find every different character that is not one of the valid DNA bases.
def find_invalid_characters(sequence):
	"""Return invalid characters in the order they first appear."""
	return list(dict.fromkeys(character for character in sequence if character not in VALID_BASES))


# Run all checks on one sequence and return both the cleaned sequence and errors.
def validate_sequence(sequence):
	"""Return the normalized sequence and any validation errors."""
	normalized = normalize_sequence(sequence)
	invalid_characters = find_invalid_characters(normalized)
	errors = []

	# Invalid characters are reported so the user knows exactly what to correct.
	if invalid_characters:
		invalid = ", ".join(repr(character) for character in invalid_characters)
		errors.append(f"Invalid character(s) found: {invalid}")

	# DNA codons contain three bases, so a complete sequence must have a length
	# that can be divided evenly by three.
	if len(normalized) % 3 != 0:
		errors.append("Sequence length is not divisible by 3")

	return normalized, errors


# Compare a sample's length and contents with the original sequence.
def classify_change(original, sample):
	"""Identify the single change type between an original and a sample."""
	original = normalize_sequence(original)
	sample = normalize_sequence(sample)

	# Check substitution first: the sequences differ but have the same length.
	if original != sample and len(original) == len(sample):
		return "substitution"
	# Check addition next: the test sequence is longer than the original.
	if len(sample) > len(original):
		return "addition"
	# Check deletion next: the test sequence is shorter than the original.
	if len(sample) < len(original):
		return "deletion"
	# If none of the change checks matched, both sequences are identical.
	return "no change"


# Load two sequence files, validate their bases, and compare their lengths/content.
def main():
	original_source = input("Enter the original sequence file path: ")
	original = read_sequence_input(original_source)
	print(f"\nStage 1 - File path received: {original_source!r}")
	print(f"Stage 2 - Sequence loaded: {len(original)} bases")

	# Compare every loaded character with the four allowed DNA bases.
	original, errors = validate_sequence(original)
	if errors:
		print("Stage 3 - Problems found")
		for error in errors:
			print(f"Error: {error}")
		return

	print("Stage 3 - Original sequence contains only valid bases")
	sample_source = input("Enter the comparison sequence file path: ")
	sample = read_sequence_input(sample_source)
	print(f"\nStage 4 - Comparison file received: {sample_source!r}")
	print(f"Stage 5 - Comparison sequence loaded: {len(sample)} bases")
	_, sample_errors = validate_sequence(sample)
	if sample_errors:
		print("Stage 6 - Comparison sequence has problems")
		for error in sample_errors:
			print(f"Error: {error}")
		return

	change = classify_change(original, sample)
	print("Stage 6 - Both sequences contain only valid bases")
	print(f"Stage 7 - Comparing sequences: {change}")
	if change == "deletion":
		print("Error: The comparison sequence contains a deletion.")
	else:
		print(f"Result: {change}")


if __name__ == "__main__":
	main()
