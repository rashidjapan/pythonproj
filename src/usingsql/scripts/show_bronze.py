"""Utility to print bronze_orders table from SQLite database."""
import sqlite3
from pathlib import Path

db = Path(__file__).parent.parent / "orders.db"
conn = sqlite3.connect(db)
cur = conn.cursor()
print(f"Database file: {db}")
print("bronze_orders contents:")
for row in cur.execute("SELECT * FROM bronze_orders"):
    print(row)
conn.close()
