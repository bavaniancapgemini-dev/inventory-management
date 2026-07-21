import tkinter as tk
from tkinter import messagebox

from database import add_product

class AddProductGUI:

    def __init__(self, refresh):

        self.refresh = refresh

        self.window = tk.Toplevel()

        self.window.title("Add Product")

        self.window.geometry("400x400")

        self.create_widgets()
        
    def create_widgets(self):

        tk.Label(

            self.window,

            text="Product Name"

        ).pack(pady=5)

        self.name = tk.Entry(

            self.window,

            width=35

        )

        self.name.pack()

        tk.Label(

            self.window,

            text="Category"

        ).pack(pady=5)

        self.category = tk.Entry(

            self.window,

            width=35

        )

        self.category.pack()

        tk.Label(

            self.window,

            text="Price"

        ).pack(pady=5)

        self.price = tk.Entry(

            self.window,

            width=35

        )

        self.price.pack()

        tk.Label(

            self.window,

            text="Quantity"

        ).pack(pady=5)

        self.quantity = tk.Entry(

            self.window,

            width=35

        )

        self.quantity.pack()

        tk.Button(

            self.window,

            text="Save Product",

            width=20,

            command=self.save_product

        ).pack(pady=20)
    
    def save_product(self):

        name = self.name.get()

        category = self.category.get()

        price = float(self.price.get())

        quantity = int(self.quantity.get())

        add_product(

            name,

            category,

            price,

            quantity

        )

        messagebox.showinfo(

            "Success",

            "Product Added Successfully"

        )

        self.refresh()

        self.window.destroy()