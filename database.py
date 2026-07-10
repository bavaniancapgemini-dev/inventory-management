import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT,

    phone TEXT,

    email TEXT,

    address TEXT

)
""")

connection.commit()
connection.close()

def add_product(name, category, price, quantity):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO products(
            name,
            category,
            price,
            quantity
        )
        VALUES(?,?,?,?)
        """,
        (
            name,
            category,
            price,
            quantity
        )
    )

    connection.commit()

    connection.close()
    
def view_products():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM products"
    )

    products = cursor.fetchall()

    connection.close()

    return products

def update_product(product_id, name, category, price, quantity):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET
            name=?,
            category=?,
            price=?,
            quantity=?
        WHERE id=?
        """,
        (
            name,
            category,
            price,
            quantity,
            product_id
        )
    )

    connection.commit()

    connection.close()
    
def delete_product(product_id):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM products WHERE id=?",

        (product_id,)

    )

    connection.commit()

    connection.close()
    
def add_customer(name, phone, email, address):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        INSERT INTO customers(

            name,

            phone,

            email,

            address

        )

        VALUES(?,?,?,?)

        """,

        (

            name,

            phone,

            email,

            address

        )

    )

    connection.commit()

    connection.close()
    
def view_customers():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "SELECT * FROM customers"

    )

    customers = cursor.fetchall()

    connection.close()

    return customers

def update_customer(customer_id, name, phone, email, address):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        UPDATE customers
        SET
            name=?,
            phone=?,
            email=?,
            address=?
        WHERE id=?
        """,

        (

            name,

            phone,

            email,

            address,

            customer_id

        )

    )

    connection.commit()

    connection.close()
    
def delete_customer(customer_id):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM customers WHERE id=?",

        (customer_id,)

    )

    connection.commit()

    connection.close()