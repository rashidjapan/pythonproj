"""Medallion architecture ETL demo: bronze -> silver -> gold using pandas."""
import os
from pathlib import Path
try:
    import pandas as pd
except ImportError:
    pd = None


def bronze_path():
    # project root is three levels up from this file (src/learning_pkg/.. -> project root)
    return Path(__file__).resolve().parent.parent.parent / 'data' / 'bronze' / 'orders_raw.csv'


def silver_path():
    return Path(__file__).resolve().parent.parent.parent / 'data' / 'silver' / 'orders_silver.csv'


def gold_path_products():
    return Path(__file__).resolve().parent.parent.parent / 'data' / 'gold' / 'gold_products.csv'


def gold_path_region():
    return Path(__file__).resolve().parent.parent.parent / 'data' / 'gold' / 'gold_region.csv'


def load_bronze():
    if pd is None:
        raise RuntimeError("pandas is required: pip install pandas")
    bp = bronze_path()
    print(f"Loading bronze data from {bp}")
    df = pd.read_csv(bp)
    return df


def transform_to_silver(df: pd.DataFrame) -> pd.DataFrame:
    # Basic cleaning: strip strings, coerce numeric, parse dates, compute order_amount if missing
    df = df.copy()
    # trim whitespace from string columns
    str_cols = ['customer_name','product_name','product_id','category','region','payment_method']
    for c in str_cols:
        if c in df.columns:
            df[c] = df[c].astype(str).str.strip()

    # quantity -> numeric (coerce non-numeric)
    df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(1).astype(int)
    # unit_price -> float
    df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0.0)
    # order_amount -> float, if missing or zero compute as quantity * unit_price
    df['order_amount'] = pd.to_numeric(df['order_amount'], errors='coerce')
    mask = df['order_amount'].isna() | (df['order_amount']==0)
    df.loc[mask, 'order_amount'] = (df.loc[mask, 'quantity'] * df.loc[mask, 'unit_price'])

    # parse order_date with multiple formats robustly
    if 'order_date' in df.columns:
        # keep original raw strings, strip whitespace and normalize separators
        raw_dates = df['order_date'].astype(str).str.strip()
        raw_dates = raw_dates.replace({'nan': None, 'None': None})
        raw_dates = raw_dates.str.replace('/', '-', regex=False)
        # normalize unusual whitespace and collapse multiple spaces
        raw_dates = raw_dates.str.replace(r'[\u3000\u00A0]', ' ', regex=True)
        raw_dates = raw_dates.str.replace(r'\s+', ' ', regex=True).str.strip()

        # try parsing with year-first / common ISO formats first
        parsed = pd.to_datetime(raw_dates, errors='coerce', dayfirst=False)

        # for remaining unparsable rows, try day-first interpretation
        bad = parsed.isna()
        if bad.any():
            parsed.loc[bad] = pd.to_datetime(raw_dates[bad].astype(str), errors='coerce', dayfirst=True)

        df['order_date'] = parsed

    # drop duplicates and reset index
    df = df.drop_duplicates(subset=['order_id']).reset_index(drop=True)
    return df


def write_silver(df: pd.DataFrame):
    sp = silver_path()
    sp.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(sp, index=False)
    print(f"Wrote silver data to {sp}")


def aggregate_gold(df: pd.DataFrame):
    gp = gold_path_products()
    gr = gold_path_region()
    gp.parent.mkdir(parents=True, exist_ok=True)

    by_product = df.groupby(['product_id','product_name','category'], as_index=False)['order_amount'].sum().sort_values('order_amount', ascending=False)
    by_region = df.groupby(['region'], as_index=False)['order_amount'].sum().sort_values('order_amount', ascending=False)

    by_product.to_csv(gp, index=False)
    by_region.to_csv(gr, index=False)
    print(f"Wrote gold product aggregates to {gp}")
    print(f"Wrote gold region aggregates to {gr}")
    return by_product, by_region


def run_etl():
    df_bronze = load_bronze()
    print('Bronze sample:')
    print(df_bronze.head())
    df_silver = transform_to_silver(df_bronze)
    print('\nSilver sample after cleaning:')
    print(df_silver.head())
    write_silver(df_silver)
    by_product, by_region = aggregate_gold(df_silver)
    print('\nTop products:')
    print(by_product.head())
    print('\nSales by region:')
    print(by_region)


if __name__ == '__main__':
    run_etl()
