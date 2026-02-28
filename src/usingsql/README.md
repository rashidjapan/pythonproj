# usingsql

Sample project demonstrating Medallion architecture using SQL (SQLite).

Structure:
- `etl.py` : Python script executing SQL statements via sqlite3 to simulate bronze/silver/gold layers.
- `orders.db` : SQLite database created by ETL.
- `scripts/` : additional SQL scripts if needed.

## Getting started

```powershell
cd src/usingsql
python etl.py   # will create or overwrite orders.db and run pipeline
sqlite3 orders.db  # open DB for manual queries
```

### Viewing bronze data

The raw bronze rows are stored inside the SQLite database file `orders.db`,
in a table called `bronze_orders`.  You can query this table directly from the
command line or with the provided helper script.

```powershell
# using sqlite3 command-line (from the usingsql folder):
sqlite3 orders.db "SELECT * FROM bronze_orders;"

# or run the Python helper which prints the path and rows:
python scripts/show_bronze.py
```

Both approaches execute the SQL statement `SELECT * FROM bronze_orders` so you
can see every record retained in the bronze layer.

Bronze data is stored in the `bronze_orders` table inside `orders.db`.

The pipeline:
1. Create `bronze_orders` table and insert raw data (includes messy values).
2. Create `silver_orders` cleaned table using SQL transformations.
3. Create gold tables (`gold_products`, `gold_region`) with aggregates.
