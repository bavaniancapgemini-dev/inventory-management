import tkinter as tk
from tkinter import messagebox

from database import update_product
from image_manager import upload_image

class EditProductGUI:

    def __init__(self, product, refresh):

        self.product = product

        self.refresh = refresh
        
        self.image = self.product[5]

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
        
        tk.Button(

            self.window,

            text="Change Image",

            width=20,

            command=self.change_image

        ).pack(pady=10)
        
        self.image_label = tk.Label(

            self.window,

            text=self.image if self.image else "No Image Selected",

            fg="blue"

        )

        self.image_label.pack()
        
    def change_image(self):

        path = upload_image()

        if path:

            self.image = path

            self.image_label.config(

                text=path

            )
        
    def update(self):

        update_product(

            self.product[0],

            self.name.get(),

            self.category.get(),

            float(self.price.get()),

            int(self.quantity.get()),
            
            self.image

        )

        messagebox.showinfo(

            "Success",

            "Product Updated Successfully"

        )

        self.refresh()

        self.window.destroy()