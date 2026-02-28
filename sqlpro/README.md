# sqlpro

Sample project demonstrating Medallion architecture using SQL (SQLite).

Structure:
- `etl.py` : Python script executing SQL statements via sqlite3 to simulate bronze/silver/gold layers.
- `orders.db` : SQLite database created by ETL.
- `scripts/` : additional SQL scripts if needed.

## Getting started

```powershell
cd sqlpro
python etl.py   # will create or overwrite orders.db and run pipeline
sqlite3 orders.db  # open DB for manual queries
```

### Viewing bronze data

After running the ETL you can inspect the raw bronze table in several ways:

```powershell
# using sqlite3 command-line
sqlite3 orders.db "SELECT * FROM bronze_orders;"

# using the helper script
python scripts/show_bronze.py
```

Bronze data is stored in the `bronze_orders` table inside `orders.db`.

The pipeline:
1. Create `bronze_orders` table and insert raw data (includes messy values).
2. Create `silver_orders` cleaned table using SQL transformations.
3. Create gold tables (`gold_products`, `gold_region`) with aggregates.
