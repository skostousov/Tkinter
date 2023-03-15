import sqlite3
conn=sqlite3.connect("customer.db")
c = conn.cursor()

c.execute("""UPDATE customers SET first_name = "John"
          WHERE rowid = 1
          
          """)


c.execute("""DELETE from customers WHERE rowid=6""")
conn.commit()
#c.execute("DROP TABLE customers")
#conn.commit()
c.execute("""SELECT rowid, * FROM customers""")
print(c.fetchall())