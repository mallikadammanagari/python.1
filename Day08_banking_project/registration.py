import csv
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
            with open ('empty.csv','a',newline="")as f:
                writer = csv.writer(f)
                writer.writerow([Name, Username, password, Balance])
            print("Registration sucessfull")
            print(customers)

    except ValueError:
        print("Please enter a valid number for balance!")

    finally:
        print("Registration process completed.")


