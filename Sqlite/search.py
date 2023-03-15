import sqlite3
conn=sqlite3.connect("customer.db")
c = conn.cursor()

c.execute("""SELECT * FROM customers WHERE last_name = 'Oppenheimer'""")
print(c.fetchall())

c.execute("""SELECT * FROM customers WHERE email LIKE 'j%'""")
print(c.fetchall())
