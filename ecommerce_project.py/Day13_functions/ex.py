# simple function/general function
#ex:1
'''def wish():
    print ('Hello World')
wish()'''
#ex:2
'''def wish():
    print ('Hello World')
wish()
wish()
wish()
wish()
wish()
wish()'''
#function with return statement
'''def wish():
    return 'Hello World'
print(wish())'''
#function with parameters
'''def wish(name):
    return 'Hello'+name
print(wish('Team'))
print(wish('james'))'''
#prime number
'''def check_prime(a):
    count=0
    i=1
    while i<=a:
        if a%i==0:
            count+=1
        i+=1
    if count==2:
        return f'{a} is a prime number'
    else:
        return f'{a} is a composite number'
print(check_prime(6))
print(check_prime(23))'''
#function with multiple return statements
'''def math(a,b):
    sum=a+b
    sub=a-b
    mult=a*b
    return sum,sub,mult
print(math(10,2))'''
#replacing the char with *
'''def replace(a):
    v='aeiouAEIOU'
    for i in a:
        if i in v:
            print('*',end='')
        else:
            print(i,end='')
    print()
print(replace('Hi there myself jameswillson'))'''
#positional arguments/keyword arguments
'''def math(a,b,c,d):
    return a+b+c+d
print (math(10,20,c=30,d=40))'''
#postional only arguments 
'''def math(a,b,c,d,/):
    print(a+b+c+d)
math(10,20,30,40)'''
#keywords only arguments
'''def math(*,a,b,c):
    print(a+b+c)
math(c=10,b=20,a=30)'''
#both postional and keyword argument 
'''def math(a,b,/,*,c,d):
    print(a+b+c+d)
math(10,20,c=30,d=40)'''

