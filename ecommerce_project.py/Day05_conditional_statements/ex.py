#if statement:
'''age=int(input('enter the value:'))
if age>=18:
    print('eligible to vote')'''
#if-else statement
'''number=10
if number%2==0:
        print('even')
else:
    print('odd')'''
#if-elif-else statement
'''marks=int(input('Enter the student marks percentage: '))
if marks>=90 and marks<=100:
          print('Grade A')
elif marks>=70 and marks<90:
       print('Grade B') 
elif marks>=50 and marks<70:
        print('Grade C')
else:
       print('Grade F')'''
#match case
day=int(input('Enter a number: '))

match day:
    case 1:
        print('Mon')
    case 2:
        print('Tus')
    case 3:
        print('Wed')
    case 4:
        print('Thru')
    case 5:
        print('Fri')
    case 6:
        print('Sat')
    case 7:
        print('Sun')
    case _:
        print('Enter a number between 1 - 7')   
