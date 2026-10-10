
from products import products


def add_to_cart(cart):
    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        if product_id not in products:
            print("Invalid product ID!")

        elif quantity <= 0:
            print("Quantity must be greater than zero!")

        else:
            cart[product_id] = cart.get(product_id, 0) + quantity
            print("Product added to cart!")

    except ValueError:
        print("Please enter numbers only.")


def view_cart(cart):
    if not cart:
        print("Your cart is empty!")
        return

    total = 0
    print("\n--- Your Shopping Cart ---")

    for product_id, quantity in cart.items():
        name, price = products[product_id]
        amount = price * quantity
        total += amount

        print(name, "x", quantity, "=", "Rs.", amount)

    print("Total Bill: Rs.", total)


def checkout(cart):
    if not cart:
        print("Your cart is empty!")
        return

    view_cart(cart)
    confirm = input("Confirm purchase? (yes/no): ").lower()

    if confirm == "yes":
        print("Order placed successfully!")
        cart.clear()
    else:
        print("Order cancelled.")
