
products = {
    1: ("Laptop", 45000),
    2: ("Mobile", 20000),
    3: ("Headphones", 1500),
    4: ("Keyboard", 1000),
    5: ("Mouse", 500)
}


def display_products():
    print("\n--- Available Products ---")

    for product_id, details in products.items():
        print(product_id, details[0], "- Rs.", details[1])
