import sqlite3


def total_revenue():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT SUM(grand_total)

        FROM bills

    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total if total else 0

def total_bills():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "SELECT COUNT(*) FROM bills"

    )

    total = cursor.fetchone()[0]

    connection.close()

    return total

def best_selling_products():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            product_name,

            SUM(quantity)

        FROM bills

        GROUP BY product_name

        ORDER BY SUM(quantity) DESC

        LIMIT 5

    """)

    data = cursor.fetchall()

    connection.close()

    return data