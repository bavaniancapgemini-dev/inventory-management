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

def sales_report():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            customer_name,

            product_name,

            quantity,

            grand_total,

            bill_date

        FROM bills

        ORDER BY bill_date DESC

    """)

    data = cursor.fetchall()

    connection.close()

    return data

def purchase_report():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT *

        FROM purchases

        ORDER BY purchase_date DESC

    """)

    data = cursor.fetchall()

    connection.close()

    return data

def customer_report():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            customer_name,

            COUNT(*),

            SUM(grand_total)

        FROM bills

        GROUP BY customer_name

    """)

    data = cursor.fetchall()

    connection.close()

    return data

def product_report():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            name,

            quantity,

            price,

            quantity*price

        FROM products

    """)

    data = cursor.fetchall()

    connection.close()

    return data

def profit_report():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "SELECT SUM(grand_total) FROM bills"

    )

    sales = cursor.fetchone()[0]

    cursor.execute(

        "SELECT SUM(total) FROM purchases"

    )

    purchases = cursor.fetchone()[0]

    connection.close()

    if sales is None:
        sales = 0

    if purchases is None:
        purchases = 0

    return sales - purchases