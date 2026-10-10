def registration_customer(customers):
    name = input("Enter your name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in customers:
        print("Username already exists!")
        return

    customers[username] = {
        "name": name,
        "password": password
    }

    print("Registration successful!")
