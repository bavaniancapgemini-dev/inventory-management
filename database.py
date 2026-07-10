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

cursor.execute("""
CREATE TABLE IF NOT EXISTS bills(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    customer_name TEXT,

    product_name TEXT,

    quantity INTEGER,

    price REAL,

    subtotal REAL,

    gst REAL,

    discount REAL,

    grand_total REAL,

    bill_date TEXT

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
    
from datetime import datetime

def add_bill(customer,
             product,
             quantity,
             price,
             gst,
             discount):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    subtotal = quantity * price

    gst_amount = subtotal * gst / 100

    discount_amount = subtotal * discount / 100

    grand_total = subtotal + gst_amount - discount_amount

    cursor.execute(
        """
        INSERT INTO bills(

            customer_name,

            product_name,

            quantity,

            price,

            subtotal,

            gst,

            discount,

            grand_total,

            bill_date

        )

        VALUES(?,?,?,?,?,?,?,?,?)
        """,

        (

            customer,

            product,

            quantity,

            price,

            subtotal,

            gst_amount,

            discount_amount,

            grand_total,

            datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        )

    )

    connection.commit()

    connection.close()

    return subtotal, gst_amount, discount_amount, grand_total
    
def get_product(product_name):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT *
        FROM products
        WHERE name=?
        """,

        (product_name,)

    )

    product = cursor.fetchone()

    connection.close()

    return product

def reduce_stock(product_name, quantity):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        UPDATE products
        SET quantity = quantity - ?
        WHERE name=?
        """,

        (

            quantity,

            product_name

        )

    )

    connection.commit()

    connection.close()