from registration import registration_customer
from login import login_customer
from withdrawal import withdraw_money
from deposit import deposit_money
customers=[]
Name=input('ENter your Name: ')
Username=input('Enter your user name: ')
password=input('Enter your password: ')
Balance=int(input('ENter your Balance: '))
customers.append([Name,Username,password,Balance])
print('registration sucessfull')
uname=input('Username: ')
pswd=input('Password: ')

if Username==uname and password==pswd:
    print('Login successfull')
    while True:
        print('''
              ----Welcome to python Bank----
              1.withdraw
              2.Diposite
              3.Balance Enqiry
              4.Exit
''')
        choice=int(input('Enter your choice: '))
        match choice:
            case 1:
                wamount=int(input('Enter your withdrawl amount: '))
                if Balance>=wamount:
                    Balance-=wamount
                    print(wamount,'is withdrwal from your account and you existing bal is: ',Balance)
                else:
                    print('Insufficent funds')
            case 2:
                Damount=int(input('Enter the diposite amount: '))
                if Damount>0:
                    Balance+=Damount
                    print('Diposite successfull and your current account balance is: ',Balance) 
                else:
                    print('Enter a valid amount')
            case 3:
                print('Your current account Balance is: ',Balance)
            case 4:
                print('Thankyou for visiting python bank have a grate day!')
                break
else:
    print('The details you have entered is invalid')   