import sqlite3

connection = sqlite3.connect("inventory.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password TEXT,

    role TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    quantity INTEGER
)
""")

try:

    cursor.execute(

        "ALTER TABLE products ADD COLUMN image TEXT"

    )

except:

    pass

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

cursor.execute("""
CREATE TABLE IF NOT EXISTS suppliers(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    company_name TEXT,

    contact_person TEXT,

    phone TEXT,

    email TEXT,

    address TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS purchases(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    supplier_name TEXT,

    product_name TEXT,

    quantity INTEGER,

    purchase_price REAL,

    total REAL,

    purchase_date TEXT

)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS stock_history(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    product_name TEXT,

    action TEXT,

    quantity INTEGER,

    date TEXT

)
""")

connection.commit()
connection.close()

def add_product(name, category, price, quantity, image):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO products(

            name,

            category,

            price,

            quantity,

            image

        )

        VALUES(?,?,?,?,?)
        """,
        (

            name,

            category,

            price,

            quantity,

            image

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

def search_product(keyword):

    import sqlite3

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

    data = cursor.fetchall()

    connection.close()

    return data

def update_product(product_id, name, category, price, quantity, image):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE products
        SET

            name=?,

            category=?,

            price=?,

            quantity=?,

            image=?

        WHERE id=?
        """,
        (

            name,

            category,

            price,

            quantity,

            image,

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
    
    cursor.execute(
        """
        UPDATE products
        SET quantity = quantity - ?
        WHERE name = ?
        """,
        (
            quantity,
            product
        )
    )
    
    cursor.execute(
        """
        INSERT INTO stock_history(

            product_name,

            action,

            quantity,

            date

        )

        VALUES(?,?,?,?)

        """,
        (
            product,
            "Sale",
            quantity,
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
    
def add_supplier(company, contact, phone, email, address):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO suppliers(
            company_name,
            contact_person,
            phone,
            email,
            address
        )
        VALUES(?,?,?,?,?)
        """,
        (
            company,
            contact,
            phone,
            email,
            address
        )
    )

    connection.commit()

    connection.close()
    
def view_suppliers():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM suppliers")

    data = cursor.fetchall()

    connection.close()

    return data

def update_supplier(supplier_id, company, contact, phone, email, address):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE suppliers
        SET
            company_name=?,
            contact_person=?,
            phone=?,
            email=?,
            address=?
        WHERE id=?
        """,
        (
            company,
            contact,
            phone,
            email,
            address,
            supplier_id
        )
    )

    connection.commit()

    connection.close()
    
def delete_supplier(supplier_id):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM suppliers WHERE id=?",

        (supplier_id,)

    )

    connection.commit()

    connection.close()
    
def search_supplier(keyword):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT *
        FROM suppliers
        WHERE company_name LIKE ?
        """,
        ("%"+keyword+"%",)
    )

    data = cursor.fetchall()

    connection.close()

    return data

from datetime import datetime

def add_purchase(

    supplier,

    product,

    quantity,

    price

):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    total = quantity * price

    date = datetime.now().strftime("%Y-%m-%d")

    cursor.execute(
        """
        INSERT INTO purchases(

            supplier_name,

            product_name,

            quantity,

            purchase_price,

            total,

            purchase_date

        )

        VALUES(?,?,?,?,?,?)
        """,
        (
            supplier,
            product,
            quantity,
            price,
            total,
            date
        )
    )

    cursor.execute(
        """
        UPDATE products

        SET quantity = quantity + ?

        WHERE name=?
        """,
        (
            quantity,
            product
        )
    )
    
    cursor.execute(
        """
        INSERT INTO stock_history(

            product_name,

            action,

            quantity,

            date

        )

        VALUES(?,?,?,?)

        """,

        (

            product,

            "Purchase",

            quantity,

            date

        )

    )

    connection.commit()

    connection.close()
    
def view_purchases():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT *

        FROM purchases

        ORDER BY id DESC

    """)

    data = cursor.fetchall()

    connection.close()

    return data

def total_purchase_cost():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT SUM(total)

        FROM purchases

    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total if total else 0

def out_of_stock():

    connection=sqlite3.connect("inventory.db")

    cursor=connection.cursor()

    cursor.execute("""

        SELECT *

        FROM products

        WHERE quantity=0

    """)

    data=cursor.fetchall()

    connection.close()

    return data

def low_stock(limit=5):

    connection=sqlite3.connect("inventory.db")

    cursor=connection.cursor()

    cursor.execute("""

        SELECT *

        FROM products

        WHERE quantity<=?

    """,(limit,))

    data=cursor.fetchall()

    connection.close()

    return data

def inventory_value():

    connection=sqlite3.connect("inventory.db")

    cursor=connection.cursor()

    cursor.execute("""

        SELECT SUM(

            quantity*price

        )

        FROM products

    """)

    total=cursor.fetchone()[0]

    connection.close()

    return total if total else 0

def product_history(product):

    connection=sqlite3.connect("inventory.db")

    cursor=connection.cursor()

    cursor.execute("""

        SELECT *

        FROM stock_history

        WHERE product_name=?

    """,(product,))

    data=cursor.fetchall()

    connection.close()

    return data

def category_report():

    connection=sqlite3.connect("inventory.db")

    cursor=connection.cursor()

    cursor.execute("""

        SELECT

            category,

            COUNT(*),

            SUM(quantity)

        FROM products

        GROUP BY category

    """)

    data=cursor.fetchall()

    connection.close()

    return data

def top_selling():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            product_name,
            SUM(quantity) AS total_sold
        FROM bills
        GROUP BY product_name
        ORDER BY total_sold DESC
        LIMIT 5
    """)

    data = cursor.fetchall()

    connection.close()

    return data

import sqlite3

def total_products():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM products")

    total = cursor.fetchone()[0]

    connection.close()

    return total


def total_customers():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM customers")

    total = cursor.fetchone()[0]

    connection.close()

    return total


def total_suppliers():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM suppliers")

    total = cursor.fetchone()[0]

    connection.close()

    return total


def total_bills():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM bills")

    total = cursor.fetchone()[0]

    connection.close()

    return total

def inventory_value():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT SUM(price * quantity)

        FROM products

    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total if total else 0

def low_stock():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT COUNT(*)

        FROM products

        WHERE quantity<=5

    """)

    total = cursor.fetchone()[0]

    connection.close()

    return total

def most_expensive():

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT name,price

        FROM products

        ORDER BY price DESC

        LIMIT 1

    """)

    product = cursor.fetchone()

    connection.close()

    return product

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

        "SELECT id,name,phone,email FROM customers"

    )

    customers = cursor.fetchall()

    connection.close()

    return customers

def search_customer(keyword):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id,name,phone,email
        FROM customers
        WHERE

            name LIKE ?

            OR phone LIKE ?

            OR email LIKE ?
        """,

        (

            "%" + keyword + "%",

            "%" + keyword + "%",

            "%" + keyword + "%"

        )

    )

    customers = cursor.fetchall()

    connection.close()

    return customers

def delete_customer(customer_id):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        "DELETE FROM customers WHERE id=?",

        (customer_id,)

    )

    connection.commit()

    connection.close()
    
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