def login_customer(customers):
    try:
        username = input("Enter username: ")
        password = input("Enter password: ")

    except Exception:
        print("Login error!")
        return None

    else:
        if username in customers and customers[username]["password"] == password:
            print("Login successful!")
            return customers[username]

        print("Invalid username or password!")
        return None

    finally:
        print("Login process completed.")
