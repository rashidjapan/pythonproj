"""Exercise 04: File I/O
Run: python exercises/04_io.py
"""


def write_and_read(path: str, text: str) -> str:
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if __name__ == "__main__":
    p = "data/sample.txt"
    content = write_and_read(p, "Hello file world")
    print(content)
