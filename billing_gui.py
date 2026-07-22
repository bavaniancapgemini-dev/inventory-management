import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from database import *

class BillingGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Billing Management")

        self.window.geometry("1100x700")

        self.items=[]

        self.create_widgets()

    def create_widgets(self):

        title=tk.Label(

            self.window,

            text="Billing Management",

            font=("Arial",20,"bold")

        )

        title.pack(pady=15)

        form=tk.Frame(self.window)

        form.pack(pady=10)

        tk.Label(form,text="Customer").grid(row=0,column=0,padx=10)

        self.customer=tk.Entry(form,width=25)

        self.customer.grid(row=0,column=1)

        tk.Label(form,text="Product").grid(row=0,column=2,padx=10)

        self.product=tk.Entry(form,width=25)

        self.product.grid(row=0,column=3)

        tk.Label(form,text="Quantity").grid(row=0,column=4,padx=10)

        self.quantity=tk.Entry(form,width=10)

        self.quantity.grid(row=0,column=5)

        tk.Button(

            form,

            text="Add Item",

            command=self.add_item

        ).grid(row=0,column=6,padx=15)

        columns=(

            "Product",

            "Quantity"

        )

        self.tree=ttk.Treeview(

            self.window,

            columns=columns,

            show="headings",

            height=15

        )

        for col in columns:

            self.tree.heading(col,text=col)

            self.tree.column(col,width=250)

        self.tree.pack(fill="both",expand=True,padx=20,pady=20)

        tk.Button(

            self.window,

            text="Create Bill",

            width=20,

            command=self.create_bill

        ).pack(pady=15)
        
    def add_item(self):

        product=self.product.get()

        quantity=self.quantity.get()

        if product=="" or quantity=="":

            messagebox.showwarning(

                "Warning",

                "Fill Product and Quantity"

            )

            return

        self.items.append(

            (

                product,

                quantity

            )

        )

        self.tree.insert(

            "",

            tk.END,

            values=(

                product,

                quantity

            )

        )

        self.product.delete(0,tk.END)

        self.quantity.delete(0,tk.END)
        
    def create_bill(self):

        messagebox.showinfo(

            "Version 28",

            "Bill calculation will be added in Version 28.1"
        )