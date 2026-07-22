import tkinter as tk
from tkinter import messagebox

from database import update_customer


class EditCustomerGUI:

    def __init__(self, customer, refresh):

        self.customer = customer

        self.refresh = refresh

        self.window = tk.Toplevel()

        self.window.title("Edit Customer")

        self.window.geometry("400x350")

        tk.Label(self.window, text="Name").pack(pady=5)

        self.name = tk.Entry(self.window, width=35)

        self.name.pack()

        self.name.insert(0, customer[1])

        tk.Label(self.window, text="Phone").pack(pady=5)

        self.phone = tk.Entry(self.window, width=35)

        self.phone.pack()

        self.phone.insert(0, customer[2])

        tk.Label(self.window, text="Email").pack(pady=5)

        self.email = tk.Entry(self.window, width=35)

        self.email.pack()

        self.email.insert(0, customer[3])

        tk.Label(self.window, text="Address").pack(pady=5)

        self.address = tk.Entry(self.window, width=35)

        self.address.pack()

        self.address.insert(0, customer[4])

        tk.Button(

            self.window,

            text="Update Customer",

            width=20,

            command=self.update

        ).pack(pady=20)

    def update(self):

        update_customer(

            self.customer[0],

            self.name.get(),

            self.phone.get(),

            self.email.get(),

            self.address.get()

        )

        messagebox.showinfo(

            "Success",

            "Customer Updated Successfully"

        )

        self.refresh()

        self.window.destroy()