import sqlite3

connection = sqlite3.connect("inventory.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(products)")

for column in cursor.fetchall():
    print(column)

connection.close()