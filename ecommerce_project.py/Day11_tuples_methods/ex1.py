'''t=(1,2,3,4,5,6)
print(type(t))'''
'''t=(1,2,3,4,5,6)
t1=()
print(type(t1))
t2=(3,)
print(type(t2))'''
#slicing operator in tuple:
'''t=(1,2,3,4,5,6,7,8,9)
t1=t[::-1]
print(t1)'''
#tuple_methods
#i)count:
'''t=(1,2,3,4,5,6,7,8,9,1)
print(t.count(1))'''
#ii)index:
#ex:1
'''t=(1,2,3,4,5,6,7,8,9,1)
print(t.index(1))
#ex:2
t=(1,2,3,4,5,6,7,8,9,1)#1-0,2-1,3-2,4-3,5-4,6-5,7-6,8-7,9-8,1-9)
print(t.index(1,1))#the last occurance of the 1 is o/p (the o/p is 9)'''
#aggregate function:
#i)sum():
'''t=(1,2,3,4,5,6,7,8,9,1)
print(sum(t))'''
#ii)max:
'''t=(1,2,3,4,5,6,7,8,9,1)
print(max(t))
'''
#iii)min():
'''t=(1,2,3,4,5,6,7,8,9,1)
print(min(t))
'''
#tuple packing:puttig multiple values into a single tuple
'''t1=1,2,3,4,5,6,7,8,9
print(type(t1))'''
#tuple unpacking :
#ex:1
'''t1=1,2,3,4,5,6,7,8,9
*a,b,c=t1
print(a)
print(b)
print(c)'''
#ex:2
'''t1=1,2,3,4,5,6,7,8,9
a,*b,c=t1
print(a)
print(b)
print(c)'''
#ex:3
'''t1=1,2,3,4,5,6,7,8,9
a,b,*c=t1
print(a)
print(b)
print(c)'''
#tuple comprehension:
'''t=(*(x for x in range(1,11)),)
print(t)'''
#traverse of tuple:
'''t=(1,2,3,4,5,6,7,8,9,10)
for i in t:
    print(i)'''
#adding two tuples and checking repeation:
'''t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)
print(t1*3)'''
#assignment:
#matrix subtraction using list:
'''l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
i=0
while i<len(l1):
    j=0
    while j<len(l1[i]):
        print(l1[i][j]-l2[i][j],end=' ')
        j+=1
    print()
    i+=1'''
#matrix addition using tuple:
'''t1=((1,2,3),(4,5,6),(7,8,9))
t2=((9,8,7),(6,5,4),(3,2,1))
i=0
while i<len(t1):
    j=0
    while j<len(t1[i]):
        print(t1[i][j]+t2[i][j],end=' ')
        j+=1
    print()
    i+=1'''

#matrix subtraction using tuple:
'''t1=((1,2,3),(4,5,6),(7,8,9))
t2=((9,8,7),(6,5,4),(3,2,1))
i=0
while i<len(t1):
    j=0
    while j<len(t1[i]):
        print(t1[i][j]-t2[i][j],end=' ')
        j+=1
    print()
    i+=1'''