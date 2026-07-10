import sqlite3

def search_product(keyword):
    
    connection = sqlite3.connect("inventory.db")
    
    cursor = connection.cursor()
    
    cursor.execute(
        """
        SELECT *
        FROM products
        WHERE name LIKE ?
        """,
        ("%"+keyword+"%",)
    )
    
    products = cursor.fetchall()
    
    connection.close()
    
    return products

import sqlite3

def search_customer(keyword):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT *
        FROM customers
        WHERE name LIKE ?
        """,

        ("%"+keyword+"%",)

    )

    customers = cursor.fetchall()

    connection.close()

    return customers