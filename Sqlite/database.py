import sqlite3
print("hello world")
#Create Database
conn = sqlite3.connect("customer.db")
#conn = sqlite3.connect(":memory:")

#Create cursor
c = conn.cursor()
#Create table
c.execute("""CREATE TABLE IF NOT EXISTS customers (
    first_name text,
    last_name text,
    email text
)""")
# Datatypes:
#NULL, INTEGER, REAL, TEXT, BLOB'

conn.commit()

#Close Connection
conn.close()