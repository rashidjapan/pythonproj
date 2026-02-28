"""ETL pipeline using SQLite to demonstrate medallion architecture."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "orders.db"

RAW_DATA = [
    (1001,101,'Alice Johnson','P001','Laptop','Electronics','1','1200.00','1200.00','2026-01-05','North','Credit Card'),
    (1002,102,'Bob Smith','P002','Mouse','Electronics','2','25','50','2026-01-06','South','Debit Card'),
    (1003,103,'Charlie Brown','P003','Desk Chair','Furniture','1','300.00','300.00','2026-01-07','East','Credit Card'),
    (1004,101,'Alice Johnson','P004','Monitor','Electronics','2','350.00','700.00','2026/01/10','North','PayPal'),
    (1005,104,'Diana Prince','P005','Keyboard','Electronics','one','80.00','80.00','2026-01-12','West','Credit Card'),
    (1006,102,'Bob Smith','P006','Desk Lamp','Furniture','3','45.00',None,'2026-01-14','South','Debit Card'),
    (1007,105,'Eve Wilson','P007','Office Desk','Furniture','1','600','600','2026-01-15','East','Credit Card'),
    (1008,103,'Charlie Brown','P008','Notebook','Stationery','10','5.00','50.00','16-01-2026','East','Cash'),
    (1009,101,'Alice Johnson','P009','Pen Set','Stationery','5','15.00','75.00','2026-01-18','North','Credit Card'),
    (1010,104,'Diana Prince','P010','Monitor Stand','Furniture','1','60.00','60.00','2026-01-20','West','Debit Card'),
]

CREATE_BRONZE = """
DROP TABLE IF EXISTS bronze_orders;
CREATE TABLE bronze_orders(
    order_id INTEGER,
    customer_id INTEGER,
    customer_name TEXT,
    product_id TEXT,
    product_name TEXT,
    category TEXT,
    quantity TEXT,
    unit_price TEXT,
    order_amount TEXT,
    order_date TEXT,
    region TEXT,
    payment_method TEXT
);
"""

CREATE_SILVER = """
DROP TABLE IF EXISTS silver_orders;
CREATE TABLE silver_orders AS
SELECT
    order_id,
    customer_id,
    TRIM(customer_name) AS customer_name,
    product_id,
    TRIM(product_name) AS product_name,
    category,
    CAST(quantity AS INTEGER) AS quantity,
    CAST(unit_price AS REAL) AS unit_price,
    CASE
      WHEN CAST(order_amount AS REAL) IS NULL OR CAST(order_amount AS REAL)=0 THEN
        CAST(quantity AS INTEGER) * CAST(unit_price AS REAL)
      ELSE CAST(order_amount AS REAL)
    END AS order_amount,
    date(substr(order_date,1,4) || '-' ||
         substr(order_date,-5,2) || '-' ||
         substr(order_date,-2,2)) AS order_date,
    region,
    payment_method
FROM bronze_orders;
"""

CREATE_GOLD = """
DROP TABLE IF EXISTS gold_products;
CREATE TABLE gold_products AS
SELECT product_id, product_name, category, SUM(order_amount) AS total_sales
FROM silver_orders
GROUP BY product_id, product_name, category
ORDER BY total_sales DESC;

DROP TABLE IF EXISTS gold_region;
CREATE TABLE gold_region AS
SELECT region, SUM(order_amount) AS total_sales
FROM silver_orders
GROUP BY region
ORDER BY total_sales DESC;
"""


def run():
    if DB_PATH.exists():
        DB_PATH.unlink()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print(f"Creating database at {DB_PATH}")
    cur.executescript(CREATE_BRONZE)
    cur.executemany("INSERT INTO bronze_orders VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", RAW_DATA)
    conn.commit()
    print("Inserted bronze rows")
    cur.executescript(CREATE_SILVER)
    conn.commit()
    print("Created silver table")
    cur.executescript(CREATE_GOLD)
    conn.commit()
    print("Created gold tables")
    # show results
    print("\nSilver sample:")
    for row in cur.execute("SELECT * FROM silver_orders LIMIT 5"):
        print(row)
    print("\nGold by product:")
    for row in cur.execute("SELECT * FROM gold_products LIMIT 5"):
        print(row)
    print("\nGold by region:")
    for row in cur.execute("SELECT * FROM gold_region"):
        print(row)
    conn.close()


if __name__ == '__main__':
    run()
