def registration_customer(customers):
    Name = input('Enter your Name: ')
    Username = input('Enter your user name: ')
    password = input('Enter your password: ')

    try:
        Balance = int(input('Enter your Balance: '))

        if Balance < 0:
            print("Invalid balance! Your account can't go below zero")
        else:
            customers.append([Name, Username, password, Balance])
            print(customers)

    except ValueError:
        print("Please enter a valid number for balance!")

    finally:
        print("Registration process completed.")

customers = []
registration_customer(customers)