import tkinter as tk
from tkinter import ttk

from database import view_bills, delete_bill


class BillHistoryGUI:

    def __init__(self):

        self.window = tk.Toplevel()

        self.window.title("Bill History")

        self.window.geometry("1000x600")
        
        search_frame = tk.Frame(self.window)

        search_frame.pack(fill="x", padx=10, pady=5)
        
        stats_frame = tk.Frame(self.window)

        stats_frame.pack(fill="x", pady=10)

        self.total_bills_label = tk.Label(

            stats_frame,

            text="Total Bills : 0",

            font=("Arial",12,"bold")

        )

        self.total_bills_label.pack(

            side="left",

            padx=20

        )

        self.total_revenue_label = tk.Label(

            stats_frame,

            text="Total Revenue : ₹0.00",

            font=("Arial",12,"bold")

        )

        self.total_revenue_label.pack(

            side="left",

            padx=20

        )

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
        
        tk.Button(

            search_frame,

            text="Refresh",

            command=self.load_bills

        ).pack(side="left", padx=10)
        
        tk.Button(

            search_frame,

            text="Delete Bill",

            bg="red",

            fg="white",

            command=self.delete_bill

        ).pack(

            side="left",

            padx=10

        )

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
        
        self.tree.bind(

            "<Double-1>",

            self.show_bill_details

        )
                
        self.load_bills()
                 
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
                
    def load_bills(self):

        for row in self.tree.get_children():

            self.tree.delete(row)

        bills = view_bills()

        revenue = 0

        for bill in bills:

            self.tree.insert(

                "",

                tk.END,

                values=bill

            )

            revenue += float(bill[4])

        self.total_bills_label.config(

            text=f"Total Bills : {len(bills)}"

        )

        self.total_revenue_label.config(

            text=f"Total Revenue : ₹{revenue:,.2f}"

        )
            
    def show_bill_details(self, event):

        selected = self.tree.focus()

        if not selected:

            return

        values = self.tree.item(selected)["values"]

        messagebox.showinfo(

            "Bill Details",

            f"""

    Bill ID : {values[0]}

    Customer : {values[1]}

    Product : {values[2]}

    Quantity : {values[3]}

    Total : ₹{values[4]}

    Date : {values[5]}

    """

        )
        
    def delete_bill(self):

        selected = self.tree.focus()

        if not selected:

            return

        values = self.tree.item(selected)["values"]

        delete_bill(values[0])

        self.load_bills()
    
from tkinter import messagebox