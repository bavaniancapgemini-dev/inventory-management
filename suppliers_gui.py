import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import *

class SuppliersGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Supplier Management")

        self.window.geometry("900x600")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(

            self.window,

            text="Supplier Management",

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

            command=self.search_supplier

        ).pack(side="left")

        button_frame = tk.Frame(self.window)

        button_frame.pack(pady=10)

        tk.Button(

            button_frame,

            text="Add Supplier",

            width=18,

            command=self.add_supplier

        ).grid(row=0,column=0,padx=10)

        tk.Button(

            button_frame,

            text="Refresh",

            width=18,

            command=self.load_suppliers

        ).grid(row=0,column=1,padx=10)

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

        self.load_suppliers()

    def add_supplier(self):

        window = tk.Toplevel(self.window)

        window.title("Add Supplier")

        window.geometry("420x420")

        tk.Label(window,text="Company Name").pack(pady=5)

        company = tk.Entry(window,width=35)

        company.pack()

        tk.Label(window,text="Contact Person").pack(pady=5)

        contact = tk.Entry(window,width=35)

        contact.pack()

        tk.Label(window,text="Phone").pack(pady=5)

        phone = tk.Entry(window,width=35)

        phone.pack()

        tk.Label(window,text="Email").pack(pady=5)

        email = tk.Entry(window,width=35)

        email.pack()

        tk.Label(window,text="Address").pack(pady=5)

        address = tk.Entry(window,width=35)

        address.pack()

        def save():

            add_supplier(

                company.get(),

                contact.get(),

                phone.get(),

                email.get(),

                address.get()

            )

            messagebox.showinfo(

                "Success",

                "Supplier Added Successfully"

            )

            window.destroy()

            self.load_suppliers()

        tk.Button(

            window,

            text="Save Supplier",

            width=20,

            command=save

        ).pack(pady=20)

    def search_supplier(self):

        pass

    def load_suppliers(self):

        for row in self.tree.get_children():

            self.tree.delete(row)

        suppliers = view_suppliers()

        for supplier in suppliers:

            self.tree.insert(

                "",

                tk.END,

                values=supplier

            )