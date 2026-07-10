import sqlite3


def register(username, password, role):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    try:

        cursor.execute(

            """
            INSERT INTO users(
                username,
                password,
                role
            )
            VALUES(?,?,?)
            """,

            (

                username,

                password,

                role

            )

        )

        connection.commit()

        print("User Created Successfully")

    except:

        print("Username Already Exists")

    connection.close()
    
def login(username, password):

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """
        SELECT role

        FROM users

        WHERE username=?

        AND password=?
        """,

        (

            username,

            password

        )

    )

    user = cursor.fetchone()

    connection.close()

    return user

def view_users():

    import sqlite3

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute("""

        SELECT

            id,

            username,

            role

        FROM users

    """)

    users = cursor.fetchall()

    connection.close()

    return users

def delete_user(user_id):

    import sqlite3

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """

        DELETE FROM users

        WHERE id=?

        """,

        (user_id,)

    )

    connection.commit()

    connection.close()
    
def change_password(username, new_password):

    import sqlite3

    connection = sqlite3.connect("inventory.db")

    cursor = connection.cursor()

    cursor.execute(

        """

        UPDATE users

        SET password=?

        WHERE username=?

        """,

        (

            new_password,

            username

        )

    )

    connection.commit()

    connection.close()