import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''Select * From stocks
             ''')
print c.fetchone()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
