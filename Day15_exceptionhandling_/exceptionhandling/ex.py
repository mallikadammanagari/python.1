#errors
#type error:
#ex-1:
'''a=10
b='minnu
print(a+b)'''
#value error
'''a=int("hello")'''
#zero division error
'''a=10
b=0
c=a/b
print(c)'''
#key error:
'''student={
    "name":"mallika",
    "age":20}
print(student['marks'])'''
#nameerror
'''print(x)'''
#index out of range error
'''numbers=[1,2,3,4,5]
print(numbers[6])'''
#exception handling
'''1.try
2.except
3.else
4.finally
'''
#ex.1
'''a=int(input('enter a value variable:'))
b=int(input('enter b value variable:'))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print('you cannot divide a value with zero')'''
#ex-2
'''try:
    a = int(input('enter a value variable: '))
    b = int(input('enter b value variable: '))
    c = a / b
    print(c)
except ZeroDivisionError:
    print('You cannot divide a value with zero.')
except ValueError:
    print('Instead of an integer, you entered a character or string.')'''
#generic errors
#method 2
'''try:
    a = int(input('enter a value variable: '))
    b = int(input('enter b value variable: '))
    c = a / b
    print(c)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)'''
#ex-2
'''try:
   a = int(input('enter a value variable: '))
   b = int(input('enter b value variable: '))
    c = a / b
    print(c)
except (ZeroDivisionError,ValueError) as e:
    print(e)'''
#method 3
'''instead of writing error we can use exception'''
'''try:
   a = int(input('enter a value variable: '))
   b = int(input('enter b value variable: '))
   c = a / b
   print(c)
except Exception as e:
    print(e)'''
#using else
'''try:
   a = int(input('enter a value variable: '))
   b = int(input('enter b value variable: '))
   c = a / b
   print(c)
except Exception as e:
    print(e)
else:
    print(c)'''
#using finally
'''try:
   a = int(input('enter a value variable: '))
   b = int(input('enter b value variable: '))
   c = a / b
   print(c)
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print('this is the end of the program')'''
#instead of printing (raise the exception)
'''try:
   a = int(input('enter a value variable: '))
   b = int(input('enter b value variable: '))
   c = a / b
   print(c)
except Exception as e:
    raise ZeroDivisionError
else:
    print(c)
finally:
    print('this is the end of the program')'''










