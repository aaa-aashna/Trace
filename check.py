import sqlite3

conn = sqlite3.connect("trace.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM activity")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()