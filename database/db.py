import sqlite3

conn = sqlite3.connect("trace.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS activity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    keystrokes INTEGER,
    active_app TEXT
)
""")

conn.commit()
conn.close()

print("Database initialized successfully!")