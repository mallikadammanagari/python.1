#Arithematic operator:
a=10
b=10
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#assignment operator:
a=10
print(a,id(a))
a+=10 
print(a,id(a))
a-=10 
a*=2  
a//=2
a%=2
print(a)
#comparison operator:
a=10
b=20
c=b>a
print(c)
d=b!=a
print(d)
#logical operator:
a=10
b=20
print(a<b and b>a)
print(a<20 or b>15)
print(not(a>b))
#membership operator:
L=[1,2,3,4,5]
print(5 in L)
print(5 not in L)
#identity operator:
a=10
b=10
print(a is b)
#identity operator:
a=10
b=15
print(a is not b)

