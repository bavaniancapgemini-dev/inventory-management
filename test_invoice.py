from invoice_generator import generate_invoice

generate_invoice(
    "Demo Customer",
    [
        ("Laptop", 1),
        ("Mouse", 2)
    ],
    52000,
    9360,
    2600,
    58760
)

print("Invoice Generated Successfully!")