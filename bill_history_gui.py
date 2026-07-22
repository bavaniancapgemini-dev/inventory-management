import tkinter as tk
from tkinter import ttk

from database import view_bills


class BillHistoryGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Bill History")

        self.window.geometry("1000x600")

        columns = (

            "ID",

            "Customer",

            "Product",

            "Quantity",

            "Total",

            "Date"

        )

        tree = ttk.Treeview(

            self.window,

            columns=columns,

            show="headings"

        )

        for col in columns:

            tree.heading(col, text=col)

            tree.column(col, width=150)

        tree.pack(fill="both", expand=True)

        for bill in view_bills():

            tree.insert("", tk.END, values=bill)