#default arugument
#ex-1
'''def math(a=1,b=1,c=1):
    print(a+b+c)
math()'''
#variable length positional arugument
#ex-1
'''def add(*args):
    print(type(args))
add(1,2,3,4,5,6,7,8,9,10)'''
#ex-2
'''def add (*args):
    sum=0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4,5,6,7,8,9,10)'''
#variable length keyword argument
#ex-1
'''def data(**kwargs):
    print(kwargs)
data(name='minnu',age=21,employeeid='minnu13',job='DA',salary=350000)'''
#ex-2
'''customers=[]
def personinfo(**kwargs):
    customers.append(kwargs)
personinfo(name='james',age=23,job='DE',salary=350000)
personinfo(name='john',age=24,job='DS',salary=40000)
print(customers)'''
#nested function
#ex-1
'''def outter():
    print('this is a outter function')
    def inner():
        print('this is a inner function')
    inner()
outter()
'''
#ex-2
'''def outter():
    print('this is a outter function')
    def inner():
        print('this is a inner function')
    return inner
outter()'''
#ex-3
'''def outter():
    print('this is a outter function')
    def inner():
        print('this is a inner function')
    return inner
outter()()'''
#closures
'''def outter(a):
    print('+'*8)
    def inner():
        print('Hello'+a)
    inner()
    print('+'*8)
outter('MALLIKA')'''
#recursive function
'''def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)
print(fact(4))
'''
#lambda function:
#ex-1
'''add=lambda x,y:x+y
print(add(10,20))'''
#ex-2
'''print((lambda x,y:x+y)(10,20))'''
#i)filter function:
'''def refine(i):
    return i%3==0
l=[1,2,3,4,5,6,7,8,9]
l2=list(filter(refine,l))
print(l2)'''
#ex-2
'''l=[1,2,3,4,5,6,7,8,9,10]
l2=list(filter(lambda x:x%3==0,l))
print(l2)'''
#ii)map function:
l=[1,2,3,4,5,6]
l2=list(map(lambda x:x**2,l))
print(l2)