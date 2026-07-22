import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from edit_customer_gui import EditCustomerGUI
from database import *

class CustomersGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Customers Management")

        self.window.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(

            self.window,

            text="Customers Management",

            font=("Arial",18,"bold")

        )

        title.pack(pady=15)
        
        search_frame = tk.Frame(self.window)

        search_frame.pack(pady=10)

        tk.Label(

            search_frame,

            text="Search"

        ).pack(side="left")

        self.search = tk.Entry(

            search_frame,

            width=35

        )

        self.search.pack(side="left", padx=10)

        tk.Button(

            search_frame,

            text="Search",

            command=self.search_customer

        ).pack(side="left")

        button_frame = tk.Frame(self.window)

        button_frame.pack(pady=10)

        tk.Button(

            button_frame,

            text="Add Customer",

            width=18,

            command=self.add_customer

        ).grid(row=0,column=0,padx=10)
        
        tk.Button(

            button_frame,

            text="Edit Customer",

            width=18,

            command=self.edit_customer

        ).grid(row=0,column=1,padx=10)
        
        tk.Button(

            button_frame,

            text="Delete Customer",

            width=18,

            command=self.delete_customer

        ).grid(row=0,column=2,padx=10)

        tk.Button(

            button_frame,

            text="Refresh",

            width=18,

            command=self.load_customers

        ).grid(row=0,column=3,padx=10)

        columns = (

            "ID",

            "Name",

            "Phone",

            "Email"

        )

        self.tree = ttk.Treeview(

            self.window,

            columns=columns,

            show="headings"

        )

        for col in columns:

            self.tree.heading(col,text=col)

            self.tree.column(col,width=180)

        self.tree.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )

        self.load_customers()

    def load_customers(self):

        for row in self.tree.get_children():

            self.tree.delete(row)

        customers = view_customers()

        for customer in customers:

            self.tree.insert(

                "",

                tk.END,

                values=customer

            )
            
    def add_customer(self):

        window = tk.Toplevel(self.window)

        window.title("Add Customer")

        window.geometry("400x350")

        tk.Label(window, text="Name").pack(pady=5)

        name = tk.Entry(window, width=35)

        name.pack()

        tk.Label(window, text="Phone").pack(pady=5)

        phone = tk.Entry(window, width=35)

        phone.pack()

        tk.Label(window, text="Email").pack(pady=5)

        email = tk.Entry(window, width=35)

        email.pack()

        tk.Label(window, text="Address").pack(pady=5)

        address = tk.Entry(window, width=35)

        address.pack()

        def save():

            add_customer(

                name.get(),

                phone.get(),

                email.get(),

                address.get()

            )

            messagebox.showinfo(

                "Success",

                "Customer Added Successfully"

            )

            window.destroy()

            self.load_customers()

        tk.Button(

            window,

            text="Save Customer",

            width=20,

            command=save

        ).pack(pady=20)
        
    def search_customer(self):

        keyword = self.search.get()

        customers = search_customer(keyword)

        for row in self.tree.get_children():

            self.tree.delete(row)

        for customer in customers:

            self.tree.insert(

                "",

                tk.END,

                values=customer

            )
            
    def delete_customer(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showwarning(

                "Warning",

                "Please select a customer."

            )

            return

        values = self.tree.item(selected)["values"]

        answer = messagebox.askyesno(

            "Delete",

            f"Delete {values[1]} ?"

        )

        if answer:

            delete_customer(values[0])

            self.load_customers()
            
    def edit_customer(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showwarning(

                "Warning",

                "Please select a customer."

            )

            return

        values = self.tree.item(selected)["values"]

        connection = sqlite3.connect("inventory.db")

        cursor = connection.cursor()

        cursor.execute(

            "SELECT * FROM customers WHERE id=?",

            (values[0],)

        )

        customer = cursor.fetchone()

        connection.close()

        EditCustomerGUI(

            customer,

            self.load_customers

        )