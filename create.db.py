import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

cursor.execute("INSERT INTO sales VALUES ('Laptop',5,50000)")
cursor.execute("INSERT INTO sales VALUES ('Mouse',10,500)")

conn.commit()
conn.close()
