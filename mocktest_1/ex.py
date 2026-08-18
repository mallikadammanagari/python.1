1.
'''a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)'''
2.
'''number=int(input('enter the number'))
if number>0:
    print('positive')
elif number<0:
    print('negative')
else:
    print('zero')'''
4.
'''num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("Largest number is:", largest)'''
7.
'''for i in range (1,6):
    for j in range (i):
      
        print('*',end=' ')
    print()
    '''
8.
'''i=1
while i<=6:
    j=1
    while j<i:
         print(j,end=' ')
         j+=1
    print( )
    i+=1'''
10
username='mallika'
password='1234'
i=1
while i<3:
    uname=(input("enter the uname:"))
    pw=(input("enter the pw:"))
    if uname==username and pw==password:
        print("login sucessful")
        break
    else:
        print("Invalid Username or Password")
        i += 1

if i > 3:
    print("Account Locked")





