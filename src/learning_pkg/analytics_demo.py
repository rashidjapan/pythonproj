"""Script to load and explore the orders dataset for analytics practice."""

try:
    import pandas as pd
except ImportError:
    pd = None


def load_orders():
    """Load the orders CSV file."""
    if pd is None:
        print("pandas is not installed. install with 'pip install pandas'")
        return None
    df = pd.read_csv("data/orders.csv")
    return df


def main() -> None:
    df = load_orders()
    if df is None:
        return
    print("Dataset shape:", df.shape)
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nDataset info:")
    print(df.info())
    print("\nBasic statistics:")
    print(df[["quantity", "unit_price", "order_amount"]].describe())
    print("\nTotal sales by region:")
    print(df.groupby("region")["order_amount"].sum())
    print("\nTotal sales by category:")
    print(df.groupby("category")["order_amount"].sum())


if __name__ == "__main__":
    main()
