def read_file(path):
    """
    Read text from a file.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, text):
    """
    Write corrected text back to file.
    """
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)