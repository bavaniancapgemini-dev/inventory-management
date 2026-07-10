from database import (
    add_product,
    view_products,
    update_product,
    delete_product,
    add_customer,
    view_customers,
    update_customer,
    delete_customer,
    add_bill,
    get_product,
    reduce_stock
)
from search import (
     search_product,
     search_customer
)
from reports import (
     total_products,
     total_customers
)
from analytics import (
    total_revenue,
    total_bills,
    best_selling_products
)


while True:

    print("\n===== INVENTORY MANAGEMENT =====")

    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Total Products")
    print("7. Add Customer")
    print("8. View Customers")
    print("9. Search Customer")
    print("10. Update Customer")
    print("11. Delete Customer")
    print("12. Total Customers")
    print("13. Generate Bill")
    print("14. Sales Analytics")
    print("15. Exit")

    choice = input("Choose: ")

    if choice == "1":

        name = input("Product Name: ")

        category = input("Category: ")

        price = float(input("Price: "))

        quantity = int(input("Quantity: "))

        add_product(
            name,
            category,
            price,
            quantity
        )

        print("✅ Product Added Successfully")
        
    elif choice == "2":
        
        products = view_products()

        print("\n===== PRODUCT LIST =====\n")

        for product in products:

            print("ID       :", product[0])

            print("Name     :", product[1])

            print("Category :", product[2])

            print("Price    : ₹", product[3])

            print("Quantity :", product[4])

            print("-" * 35)
            
    elif choice == "3":

        keyword = input("Enter Product Name: ")

        products = search_product(keyword)

        print("\n===== SEARCH RESULTS =====\n")

        if len(products) == 0:

            print("No Product Found")

        else:

            for product in products:

                print("ID       :", product[0])

                print("Name     :", product[1])

                print("Category :", product[2])

                print("Price    : ₹", product[3])

                print("Quantity :", product[4])

                print("-"*35)
                
    elif choice == "4":

        product_id = int(input("Enter Product ID: "))

        name = input("New Product Name: ")

        category = input("New Category: ")

        price = float(input("New Price: "))

        quantity = int(input("New Quantity: "))

        update_product(

            product_id,

            name,

            category,

            price,

            quantity

        )

        print("✅ Product Updated Successfully")
        
    elif choice == "5":

        product_id = int(input("Enter Product ID to Delete: "))

        delete_product(product_id)

        print("✅ Product Deleted Successfully")
        
    elif choice == "6":

        print("\n===== INVENTORY REPORT =====")

        print("Total Products:", total_products())
        
    elif choice=="7":

        name=input("Customer Name: ")

        phone=input("Phone Number: ")

        email=input("Email: ")

        address=input("Address: ")

        add_customer(

            name,

            phone,

            email,

            address

        )

        print("Customer Added Successfully")
        
    elif choice=="8":

        customers = view_customers()

        print("\n===== CUSTOMER LIST =====\n")

        if len(customers) == 0:

            print("No Customers Found")

        else:

            for customer in customers:

                print("ID      :", customer[0])

                print("Name    :", customer[1])

                print("Phone   :", customer[2])

                print("Email   :", customer[3])

                print("Address :", customer[4])

                print("-"*40)
                
    elif choice=="9":

        keyword = input("Enter Customer Name: ")

        customers = search_customer(keyword)

        print("\n===== SEARCH RESULTS =====\n")

        if len(customers) == 0:

            print("No Customer Found")

        else:

            for customer in customers:

                print("ID      :", customer[0])

                print("Name    :", customer[1])

                print("Phone   :", customer[2])

                print("Email   :", customer[3])

                print("Address :", customer[4])

                print("-"*40)
                
    elif choice=="10":

        customer_id = int(input("Customer ID: "))

        name = input("New Name: ")

        phone = input("New Phone: ")

        email = input("New Email: ")

        address = input("New Address: ")

        update_customer(

            customer_id,

            name,

            phone,

            email,

            address

        )

        print("✅ Customer Updated Successfully")
        
    elif choice=="11":

        customer_id = int(input("Customer ID: "))

        delete_customer(customer_id)

        print("✅ Customer Deleted Successfully")
        
    elif choice=="12":

        print("\n===== CUSTOMER REPORT =====")

        print(

            "Total Customers:",

            total_customers()

        )
        
    elif choice=="13":

        customer = input("Customer Name: ")

        product = input("Product Name: ")

        quantity = int(input("Quantity: "))
        
        gst = float(input("GST % : "))
        
        discount = float(input("Discount % : "))

        data = get_product(product)

        if data is None:

            print("❌ Product Not Found")

        else:

            stock = data[4]      # quantity column

            price = data[3]      # price column

            if quantity > stock:

                print("❌ Not Enough Stock")

            else:

                subtotal, gst_amount, discount_amount, grand_total = add_bill(

                    customer,

                    product,

                    quantity,

                    price,

                    gst,

                    discount

                )

                reduce_stock(

                    product,

                    quantity

                )

                print()

                print("========== INVOICE ==========")

                print("Customer :", customer)

                print("Product  :", product)

                print("Price    :", price)

                print("Quantity :", quantity)

                print("-----------------------------")

                print(f"Subtotal : ₹{subtotal:.2f}")

                print(f"GST      : ₹{gst_amount:.2f}")

                print(f"Discount : ₹{discount_amount:.2f}")

                print("-----------------------------")

                print(f"TOTAL    : ₹{grand_total:.2f}")

                print("=============================")
                
    elif choice=="14":

        print()

        print("===== SALES ANALYTICS =====")

        print()

        print("Total Revenue : ₹", total_revenue())

        print("Bills Generated :", total_bills())

        print()

        print("Best Selling Products")

        print("--------------------------")

        for item in best_selling_products():

            print(

                item[0],

                "->",

                item[1],

                "Sold"

            )

        print()
    
    elif choice == "15":

        break

    else:

        print("Invalid Choice")