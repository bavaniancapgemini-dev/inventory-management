import tkinter as tk
from tkinter import ttk, messagebox

from database import (
    view_products,
    search_product,
    delete_product
)
from add_product_gui import AddProductGUI
from edit_product_gui import EditProductGUI
from PIL import Image
from PIL import ImageTk

class ProductsGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Products Management")

        self.window.geometry("1000x600")

        self.create_widgets()

        self.load_products()
        
    def create_widgets(self):

        top = tk.Frame(self.window)

        top.pack(fill="x", pady=10)

        tk.Label(

            top,

            text="Search Product"

        ).pack(side="left", padx=5)

        self.search = tk.Entry(

            top,

            width=40

        )

        self.search.pack(side="left")

        tk.Button(

            top,

            text="Search",

            command=self.search_products

        ).pack(side="left", padx=10)
        
        columns = (

            "ID",

            "Name",

            "Category",

            "Price",

            "Quantity"

        )

        self.tree = ttk.Treeview(

            self.window,

            columns=columns,

            show="headings"

        )
        
        self.image_label = tk.Label(

            self.window,

            text="No Image",

            width=25,

            height=15,

            relief="solid"

        )

        self.image_label.pack(

            side="right",

            padx=20,

            pady=20

        )
        
        self.tree.bind(

            "<<TreeviewSelect>>",

            self.show_image

        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(col, width=180)

        self.tree.pack(

            fill="both",

            expand=True,

            padx=10,

            pady=10

        )
        bottom = tk.Frame(self.window)

        bottom.pack(pady=10)

        tk.Button(

            bottom,

            text="Add Product",

            width=15,

            command=self.add_product

        ).grid(row=0,column=0,padx=5)

        tk.Button(

            bottom,

            text="Edit Product",

            width=15,

            command=self.edit_product

        ).grid(row=0,column=1,padx=5)

        tk.Button(

            bottom,

            text="Delete Product",

            width=15,

            command=self.delete_selected

        ).grid(row=0,column=2,padx=5)

        tk.Button(

            bottom,

            text="Refresh",

            width=15,

            command=self.load_products

        ).grid(row=0,column=3,padx=5)
        
    def load_products(self):

        for row in self.tree.get_children():

            self.tree.delete(row)

        products = view_products()

        for product in products:

            self.tree.insert(

                "",

                "end",

                values=(

                    product[0],

                    product[1],

                    product[2],

                    product[3],

                    product[4]

                )

            )

    def search_products(self):

        keyword = self.search.get()

        for row in self.tree.get_children():

            self.tree.delete(row)

        products = search_product(keyword)

        for product in products:

            self.tree.insert(

                "",

                "end",

                values=(

                    product[0],

                    product[1],

                    product[2],

                    product[3],

                    product[4]

                )

            )

    def add_product(self):

        AddProductGUI(

            self.load_products

        )

    def edit_product(self):

        selected = self.tree.focus()

        if not selected:

            messagebox.showwarning(

                "Warning",

                "Please select a product."

            )

            return

        values = self.tree.item(selected)["values"]

        products = view_products()

        for product in products:

            if product[0] == values[0]:

                EditProductGUI(

                    product,

                    self.load_products

                )

                break

    def delete_selected(self):

        pass
    
    def show_image(self, event):

        selected = self.tree.focus()

        if not selected:

            return

        values = self.tree.item(selected)["values"]

        products = view_products()

        image_path = ""

        for product in products:

            if product[0] == values[0]:

                image_path = product[5]

                break

        if image_path == "":

            self.image_label.config(

                image="",

                text="No Image"

            )

            return

        try:

            image = Image.open(image_path)

            image = image.resize((180,180))

            photo = ImageTk.PhotoImage(image)

            self.image_label.configure(

                image=photo,

                text=""

            )

            self.image_label.image = photo

        except Exception as e:

            print(e)

            self.image_label.config(

                image="",

                text="Image Not Found"

            )