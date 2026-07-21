import tkinter as tk
from tkinter import messagebox

from database import update_product

class EditProductGUI:

    def __init__(self, product, refresh):

        self.product = product

        self.refresh = refresh

        self.window = tk.Toplevel()

        self.window.title("Edit Product")

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

        self.name.insert(0, self.product[1])


        tk.Label(

            self.window,

            text="Category"

        ).pack(pady=5)

        self.category = tk.Entry(

            self.window,

            width=35

        )

        self.category.pack()

        self.category.insert(0, self.product[2])

        tk.Label(

            self.window,

            text="Price"

        ).pack(pady=5)

        self.price = tk.Entry(

            self.window,

            width=35

        )

        self.price.pack()

        self.price.insert(0, self.product[3])


        tk.Label(

            self.window,

            text="Quantity"

        ).pack(pady=5)

        self.quantity = tk.Entry(

            self.window,

            width=35

        )

        self.quantity.pack()

        self.quantity.insert(0, self.product[4])

        tk.Button(

            self.window,

            text="Update Product",

            width=20,

            command=self.update

        ).pack(pady=20)
        
    def update(self):

        update_product(

            self.product[0],

            self.name.get(),

            self.category.get(),

            float(self.price.get()),

            int(self.quantity.get())

        )

        messagebox.showinfo(

            "Success",

            "Product Updated Successfully"

        )

        self.refresh()

        self.window.destroy()