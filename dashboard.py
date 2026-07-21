import tkinter as tk


class Dashboard:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Inventory Management System")

        self.window.geometry("900x600")

        self.window.configure(bg="#ecf0f1")

        title = tk.Label(

            self.window,

            text="Inventory Management Dashboard",

            font=("Arial", 22, "bold"),

            bg="#2c3e50",

            fg="white",

            pady=15

        )

        title.pack(fill="x")

        frame = tk.Frame(self.window, bg="#ecf0f1")

        frame.pack(pady=40)

        tk.Button(

            frame,

            text="Products",

            width=20,

            height=2,

            command=self.products

        ).grid(row=0,column=0,padx=15,pady=15)

        tk.Button(

            frame,

            text="Customers",

            width=20,

            height=2,

            command=self.customers

        ).grid(row=0,column=1,padx=15,pady=15)

        tk.Button(

            frame,

            text="Billing",

            width=20,

            height=2,

            command=self.billing

        ).grid(row=1,column=0,padx=15,pady=15)

        tk.Button(

            frame,

            text="Suppliers",

            width=20,

            height=2,

            command=self.suppliers

        ).grid(row=1,column=1,padx=15,pady=15)

        tk.Button(

            frame,

            text="Reports",

            width=20,

            height=2,

            command=self.reports

        ).grid(row=2,column=0,padx=15,pady=15)

        tk.Button(

            frame,

            text="Logout",

            width=20,

            height=2,

            command=self.window.destroy

        ).grid(row=2,column=1,padx=15,pady=15)

        self.window.mainloop()

    def products(self):

        from products_gui import ProductsGUI

        ProductsGUI()

    def customers(self):

        print("Customers Module")

    def billing(self):

        print("Billing Module")

    def suppliers(self):

        print("Suppliers Module")

    def reports(self):

        print("Reports Module")