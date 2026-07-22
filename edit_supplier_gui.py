import tkinter as tk
from tkinter import messagebox

from database import update_supplier


class EditSupplierGUI:

    def __init__(self, supplier, refresh):

        self.supplier = supplier

        self.refresh = refresh

        self.window = tk.Toplevel()

        self.window.title("Edit Supplier")

        self.window.geometry("450x420")

        tk.Label(self.window, text="Company Name").pack(pady=5)

        self.company = tk.Entry(self.window, width=35)

        self.company.pack()

        self.company.insert(0, supplier[1])

        tk.Label(self.window, text="Contact Person").pack(pady=5)

        self.contact = tk.Entry(self.window, width=35)

        self.contact.pack()

        self.contact.insert(0, supplier[2])

        tk.Label(self.window, text="Phone").pack(pady=5)

        self.phone = tk.Entry(self.window, width=35)

        self.phone.pack()

        self.phone.insert(0, supplier[3])

        tk.Label(self.window, text="Email").pack(pady=5)

        self.email = tk.Entry(self.window, width=35)

        self.email.pack()

        self.email.insert(0, supplier[4])

        tk.Label(self.window, text="Address").pack(pady=5)

        self.address = tk.Entry(self.window, width=35)

        self.address.pack()

        self.address.insert(0, supplier[5])

        tk.Button(

            self.window,

            text="Update Supplier",

            width=20,

            command=self.update

        ).pack(pady=20)

    def update(self):

        update_supplier(

            self.supplier[0],

            self.company.get(),

            self.contact.get(),

            self.phone.get(),

            self.email.get(),

            self.address.get()

        )

        messagebox.showinfo(

            "Success",

            "Supplier Updated Successfully"

        )

        self.refresh()

        self.window.destroy()