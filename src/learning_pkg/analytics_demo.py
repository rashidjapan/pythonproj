"""Script to load and explore the orders dataset for analytics practice."""

import os
try:
    import pandas as pd
except ImportError:
    pd = None


def load_orders():
    """Load the orders CSV file."""
    if pd is None:
        print("pandas is not installed. install with 'pip install pandas'")
        return None
    # construct path relative to this script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "..", "..", "data", "orders.csv")
    df = pd.read_csv(data_path)
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
    
    # print(f"\n df details : {df}" )
    print("\nTotal sales by region:")
    print(df.groupby("region")["order_amount"].sum())
    print("\nTotal sales by category:")
    print(df.groupby("category")["order_amount"].sum())    
    print("\nTop 5 products by sales:")    
    print(df.groupby("product_name")["order_amount"].sum().sort_values(ascending=False).head())  
    print("\nDistinct product names:")
    print(df["product_name"].drop_duplicates().reset_index(drop=True))
    

if __name__ == "__main__":
    main()
