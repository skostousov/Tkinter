import sqlite3
conn=sqlite3.connect("customer.db")
c = conn.cursor()
many_customers = [("Mary", "Oppenheimer", "mopp@gmail.com"), ("Jane", "oppenheimer", "jopp@gmail.com"), ("Steve", "Miller", "steve.miller@hotmail.com"),]
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)
conn.commit()
conn.close()