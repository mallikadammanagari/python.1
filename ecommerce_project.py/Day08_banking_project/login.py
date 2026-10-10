def login_customer(customers):

    try:
        uname = input("Username: ")
        pword = input("Password: ")

    except Exception:
        print("Login error!")
        return None

    else:
        for customer in customers:
            if customer[1] == uname and customer[2] == pword:
                print("Login successful")
                return customer

        print("Invalid username or password")
        return None

    finally:
        print("Login process completed.\n")


