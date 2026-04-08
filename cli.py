import sys
from io import read_file, write_file
from editor import interactive_edit


def main():
    if len(sys.argv) < 2:
        print("Usage: orthos <file>")
        sys.exit(1)

    filepath = sys.argv[1]

    text = read_file(filepath)

    print("Loaded file:", filepath)

    corrected_text = interactive_edit(text)

    write_file(filepath, corrected_text)

    print("\nFile updated.")


if __name__ == "__main__":
    main()