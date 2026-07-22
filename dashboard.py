import tkinter as tk
from datetime import datetime
from theme import *
from database import *

from tkinter import messagebox

from tkinter import ttk

class Dashboard:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Inventory Management System")

        self.window.geometry("1200x700")

        self.window.configure(bg=BACKGROUND)
        
        self.main = tk.Frame(

            self.window,

            bg=BACKGROUND

        )

        self.main.pack(

            fill="both",

            expand=True

        )

        self.left = tk.Frame(

            self.main,

            bg=PRIMARY,

            width=240

        )

        self.left.pack(

            side="left",

            fill="y"

        )

        self.left.pack_propagate(False)

        self.right = tk.Frame(

            self.main,

            bg=BACKGROUND

        )

        self.right.pack(

            side="right",

            fill="both",

            expand=True

        )

        title = tk.Label(

            self.right,

            text="Inventory Management Dashboard",

            font=("Arial", 22, "bold"),

            bg="#2c3e50",

            fg="white",

            pady=15

        )

        title.pack(fill="x")
        
        welcome_frame = tk.Frame(

            self.right,

            bg=BACKGROUND

        )

        welcome_frame.pack(

            fill="x",

            padx=20,

            pady=15

        )

        self.welcome = tk.Label(

            welcome_frame,

            text="Welcome, Admin 👋",

            font=("Arial",16,"bold"),

            bg=BACKGROUND,

            fg=TEXT

        )

        self.welcome.pack(

            side="left"
        )
        
        self.clock = tk.Label(

            welcome_frame,

            font=("Arial",12),

            bg=BACKGROUND,

            fg="gray"

        )

        self.clock.pack(

            side="right"
        )
        
        cards = tk.Frame(

            self.right,

            bg=BACKGROUND

        )

        cards.pack(

            pady=30
        )
        
        actions = tk.Frame(

            self.right,

            bg=BACKGROUND

        )

        actions.pack(

            pady=25
        )
        
        tk.Button(

            actions,

            text="➕ Add Product",

            width=18,

            height=2,

            bg=SUCCESS,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            command=self.products

        ).grid(

            row=0,

            column=0,

            padx=15,

            pady=10

        )
        
        tk.Button(

            actions,

            text="🧾 Create Bill",

            width=18,

            height=2,

            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            command=self.billing

        ).grid(

            row=0,

            column=1,

            padx=15,

            pady=10

        )
        
        tk.Button(

            actions,

            text="👥 Add Customer",

            width=18,

            height=2,

            bg=WARNING,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            command=self.customers

        ).grid(

            row=1,

            column=0,

            padx=15,

            pady=10

        )
        
        tk.Button(

            actions,

            text="🚚 Add Supplier",

            width=18,

            height=2,

            bg=DANGER,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            command=self.suppliers

        ).grid(

            row=1,

            column=1,

            padx=15,

            pady=10

        )
        
        product_card = tk.Frame(

            cards,

            bg="white",

            relief="raised",

            bd=2,

            width=180,

            height=120

        )

        product_card.grid(row=0,column=0,padx=15)

        product_card.pack_propagate(False)

        tk.Label(

            product_card,

            text="Products",

            font=("Arial",13,"bold"),

            bg="white"

        ).pack(pady=10)

        tk.Label(

            product_card,

            text=str(total_products()),

            font=("Arial",28,"bold"),

            fg=PRIMARY,

            bg="white"

        ).pack()
        
        value_card = tk.Frame(

            cards,

            bg="white",

            relief="raised",

            bd=2,

            width=180,

            height=120

        )

        value_card.grid(

            row=0,

            column=1,

            padx=15

        )

        value_card.pack_propagate(False)

        tk.Label(

            value_card,

            text="Inventory Value",

            font=("Arial",13,"bold"),

            bg="white"

        ).pack(pady=10)

        tk.Label(

            value_card,

            text=f"₹ {inventory_value():,.0f}",

            font=("Arial",20,"bold"),

            fg=SUCCESS,

            bg="white"

        ).pack()
        
        stock_card = tk.Frame(

            cards,

            bg="white",

            relief="raised",

            bd=2,

            width=180,

            height=120

        )

        stock_card.grid(

            row=0,

            column=2,

            padx=15

        )

        stock_card.pack_propagate(False)

        tk.Label(

            stock_card,

            text="Low Stock",

            font=("Arial",13,"bold"),

            bg="white"

        ).pack(pady=10)

        tk.Label(

            stock_card,

            text=str(low_stock()),

            font=("Arial",22,"bold"),

            fg=DANGER,

            bg="white"

        ).pack()
        
        expensive = most_expensive()

        exp_card = tk.Frame(

            cards,

            bg="white",

            relief="raised",

            bd=2,

            width=220,

            height=120

        )

        exp_card.grid(

            row=0,

            column=3,

            padx=15

        )

        exp_card.pack_propagate(False)

        tk.Label(

            exp_card,

            text="Top Product",

            font=("Arial",13,"bold"),

            bg="white"

        ).pack(pady=8)

        if expensive:

            tk.Label(

                exp_card,

                text=expensive[0],

                bg="white",

                font=("Arial",11,"bold")

            ).pack()

            tk.Label(

                exp_card,

                text=f"₹ {expensive[1]:,.2f}",

                fg=PRIMARY,

                bg="white",

                font=("Arial",12)

            ).pack()
        
        logo = tk.Label(

            self.left,

            text="📦 Inventory",

            bg=PRIMARY,

            fg="white",

            font=("Arial",18,"bold"),

            pady=25

        )

        logo.pack()

        frame = tk.Frame(self.left, bg=PRIMARY)

        frame.pack(pady=40)

        tk.Button(

            frame,

            text="Products",

            width=20,

            height=2,

            command=self.products,
            
            bg=PRIMARY,
            
            fg="white",
            
            font=("Arial",11,"bold"),
            
            relief="flat",
            
            activebackground=SECONDARY,
            
            activeforeground="white"

        ).grid(row=0,column=0,padx=15,pady=15)

        tk.Button(

            frame,

            text="Customers",

            width=20,

            height=2,

            command=self.customers,
            
            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            activebackground=SECONDARY,

            activeforeground="white"

        ).grid(row=0,column=1,padx=15,pady=8)

        tk.Button(

            frame,

            text="Billing",

            width=20,

            height=2,

            command=self.billing,
            
            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            activebackground=SECONDARY,

            activeforeground="white"

        ).grid(row=1,column=0,padx=15,pady=8)

        tk.Button(

            frame,

            text="Suppliers",

            width=20,

            height=2,

            command=self.suppliers,
            
            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            activebackground=SECONDARY,

            activeforeground="white"

        ).grid(row=1,column=1,padx=15,pady=8)

        tk.Button(

            frame,

            text="Reports",

            width=20,

            height=2,

            command=self.reports,
            
            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            activebackground=SECONDARY,

            activeforeground="white"

        ).grid(row=2,column=0,padx=15,pady=8)

        tk.Button(

            frame,

            text="Logout",

            width=20,

            height=2,

            command=self.window.destroy,
            
            bg=PRIMARY,

            fg="white",

            font=("Arial",11,"bold"),

            relief="flat",

            activebackground=SECONDARY,

            activeforeground="white"

        ).grid(row=2,column=1,padx=15,pady=8)
        
        self.update_clock()

        self.window.mainloop()

    def products(self):

        from products_gui import ProductsGUI

        ProductsGUI()

    def customers(self):

        from customers_gui import CustomersGUI
        
        CustomersGUI()

    def billing(self):

        from billing_gui import BillingGUI

        BillingGUI()
    
    def suppliers(self):

        from suppliers_gui import SuppliersGUI
        
        SuppliersGUI()

    def reports(self):

        print("Reports Module")
        
    def update_clock(self):

        now = datetime.now().strftime("%d-%m-%Y   %I:%M:%S %p")

        self.clock.config(

            text=now

        )

        self.window.after(

            1000,

            self.update_clock

        )