def deposit_money(customer):
    try:
        amount = int(input("Enter deposit amount: "))

    except ValueError:
        print("Enter numbers only.")

    else:
        if amount > 0:
            customer[3] += amount
            print("Deposit successful.")
            print("Current balance:", customer[3])

        else:
            print("Deposit amount must be greater than 0.")

    finally:
        print("Transaction completed.")
customers = ["minnu", "meowmeow", "1234", 30000]
deposit_money(customers)