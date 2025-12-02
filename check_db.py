import sqlite3

conn = sqlite3.connect('housing.db')
cursor = conn.cursor()
# Select everyone who is an officer (Rank starts with 'O')
cursor.execute("SELECT * FROM SERVICE_MEMBERS")
rows = cursor.fetchall()

print("--- CURRENT DATABASE DATA ---")
for row in rows:
    print(row)

conn.close()