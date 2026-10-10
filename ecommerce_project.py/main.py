
from registration import registration_customer
from login import login_customer
from products import display_products
from cart import add_to_cart, view_cart, checkout

customers = {}
cart = {}

while True:
    print("""
    --- Welcome to Python E-Commerce ---

    1. Register
    2. Login
    3. Exit
    """)

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    match choice:
        case 1:
            registration_customer(customers)

        case 2:
            customer = login_customer(customers)

            if customer is not None:
                while True:
                    print("""
                    --- Customer Menu ---

                    1. View Products
                    2. Add to Cart
                    3. View Cart
                    4. Checkout
                    5. Logout
                    """)

                    try:
                        option = int(input("Enter your choice: "))
                    except ValueError:
                        print("Enter a valid number.")
                        continue

                    match option:
                        case 1:
                            display_products()

                        case 2:
                            display_products()
                            add_to_cart(cart)

                        case 3:
                            view_cart(cart)

                        case 4:
                            checkout(cart)

                        case 5:
                            print("Logged out successfully!")
                            break

                        case _:
                            print("Invalid choice!")

        case 3:
            print("Thank you for visiting Python E-Commerce!")
            break

        case _:
            print("Invalid choice!")
