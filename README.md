# first-strand

## Run the checker

```bash
python3 strandcheck.py
```

At each prompt, enter either a DNA sequence or the path to a text file containing
one sequence. Example paths are stored in the `sequence/` folder:

```text
sequence/original.txt
sequence/sample_no_change.txt
sequence/sample_substitution.txt
sequence/sample_addition.txt
sequence/sample_deletion.txt
```

Each file should contain DNA bases using `A`, `T`, `C`, and `G`. Lines are joined
when a downloaded sequence wraps across multiple lines.