import tkinter as tk
from datetime import datetime
from theme import *
from database import *

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

        print("Customers Module")

    def billing(self):

        print("Billing Module")

    def suppliers(self):

        print("Suppliers Module")

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