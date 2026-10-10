#pancard
'''import re
pan=input("enter a pan card number:")
res=re.fullmatch(r'[A-Z]{4}[0-9]{5}[A-Z]',pan)
print(res)
if res:
    print("Valid Pan Card number")
else:
    print("Invalid Pan Card number")
#password'''
'''import re 
pswd=input("enter a password:")
res=re.fullmatch(r'[A-Z]{1}[a-z]{4}[@#$%]{1}[0-9]{3}',pswd)
print(res)
if res:
    print("the password you entered is correct")
else:
    print("incorrect password")'''
#phonenumber
'''import re
PNO=input("enter a phone number:")
res=re.fullmatch(r'\d{10}',PNO)
print(res)
if res:
    print("valid phone number")
else:
    print("invalid phone number")'''
#email.id
'''import re
EmailID = input("Enter the email ID: ")
res = re.fullmatch(r'\w+@\w+\.\w+', EmailID)
print(res)
if res:
    print("Valid Email ID")
else:
    print("Invalid Email ID")'''

