import sqlite3

def total_products():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")

    total = cursor.fetchone()[0]

    connection.close()

    return total

import sqlite3

def total_customers():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM customers"

    )

    total = cursor.fetchone()[0]

    connection.close()

    return total