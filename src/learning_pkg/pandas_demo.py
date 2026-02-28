"""Simple Pandas learning script. Run as module or script."""

# pandas may not be installed; guard against ImportError
try:
    import pandas as pd
except ImportError:
    pd = None


def main() -> None:
    if pd is None:
        print("pandas is not installed. install with 'pip install pandas'")
        return
    # create a simple DataFrame
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
    })
    print("DataFrame:\n", df)
    print("Mean age:", df["age"].mean())


if __name__ == "__main__":
    main()
