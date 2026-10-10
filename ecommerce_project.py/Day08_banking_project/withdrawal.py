def withdraw_money(customer):
    try:
        amount = int(input("Enter withdrawal amount: "))

    except ValueError:
        print("Enter numbers only.")

    else:
        if amount <= 0:
            print("Invalid amount")
        elif customer[3] >= amount:
            customer[3] -= amount
            print("Withdrawal successful")
            print("Current balance:", customer[3])
        else:
            print("Insufficient balance")

    finally:
        print("Transaction completed")

