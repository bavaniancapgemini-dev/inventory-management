import tkinter as tk
from tkinter import ttk

from database import view_bills


class BillHistoryGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Bill History")

        self.window.geometry("1000x600")
        
        search_frame = tk.Frame(self.window)

        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(

            search_frame,

            text="Search Customer:"

        ).pack(side="left")

        self.search = tk.Entry(search_frame)

        self.search.pack(

            side="left",

            padx=10

        )

        tk.Button(

            search_frame,

            text="Search",

            command=self.search_bill

        ).pack(side="left")

        columns = (

            "ID",

            "Customer",

            "Product",

            "Quantity",

            "Total",

            "Date"

        )

        self.tree = ttk.Treeview(

            self.window,

            columns=columns,

            show="headings"

        )

        for col in columns:

            self.tree.heading(col, text=col)

            self.tree.column(col, width=150)

        self.tree.pack(fill="both", expand=True)

        for bill in view_bills():

            self.tree.insert("", tk.END, values=bill)
            
    def search_bill(self):

        keyword = self.search.get().lower()

        for row in self.tree.get_children():

            self.tree.delete(row)

        for bill in view_bills():

            if keyword in str(bill[1]).lower():

                self.tree.insert(

                    "",

                    tk.END,

                    values=bill

                )