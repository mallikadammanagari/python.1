#string formatting methods:
#c-style foramtting :
#%s-string ,%i-integer,%f,%F%g-float
'''product='Hard disk'
size=500
price=199.23
print('%s of %i GB is costing about %g dollers'%(product,size,price))'''
#.format:
#{ } consider as placeholders which holds the value pof index
'''product='Hard disk'
size=500
price=199.23
print('{1} of {2} GB is costing about {0} dollers'.format(price,product,size))
'''
#formatted string:
'''product='Hard disk'
size=500
price=199.23
print(f'{product} of {size} is costing about {price} dollers')'''
#list:
#ex:1
'''l=[10,23,54,23+9j,True,'list',10]'''
'''for i in l:
    print(i)'''
#ex:2
'''l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
print(l1*3)'''
#slicing operator:
#ex:1
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[2:]#starts from 2nd index with is 3
print(l1)'''
#ex:2
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[0::4]#::skips 
print(l1)'''
#ex:3
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[0:6] #sarts from  0 index and ends at 6 index
print(l1)
'''
#ex:4
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[:6]#stops at 6 th index
print(l1)
'''
#ex:5
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[0:7:1]#0 is start,7is stop,1 is step
print(l1)'''
#ex:6
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[0:6:3]#0 is start,6 is stop,3 is step
print(l1)'''
#ex:7
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l[::-1]#-1 refers to reverse
print(l1)
'''
#list methods:
#i)append():adds one element at the end of the list
'''l=[1,2,3,4,5,6,7,8,9,10]
l.append(11)
print(l)
print(id(l))'''
#ii)copy:returns a shallow copy of the list
'''l=[1,2,3,4,5,6,7,8,9,10]
l1=l
l2=l.copy()
print(id(l))
print(id(l2))
print(l2)
'''
#iii)extend:adds a sequence at the end of the list
'''l=[1,2,3,4,5,6,7,8,9,10]
l.extend('python')
print(l)'''
#iv)insert:at a sepcific index
'''l=[1,2,3,4,5,6,7,8,9,10]
l.insert(0,15)
print(l)'''
#v)count:
'''l=[1,2,2,3,2]
print(l.count(2))'''
#vi)index:returns the index of first occurance value
'''l=[1,2,3,4,5,6,7,8,9,10,3]
l1=l.index(3)
print(l1)
'''
#vii)pop:removes the last elements
'''l=[1,2,3,4,5,6,7,8,9,10]
l.pop()
print(l)'''
#viii)remove:removing the element based on given value from the list
'''l=[1,2,3,4,5,6,7,8,9,10]
l.remove(6)
print(l)'''
#ix)reverse:
'''l=[1,2,3,4,5,6,7,8,9,10]
l.reverse()
print(l)'''
#x)sort:arranging in ascending and descending order
'''l=[90,20,40,70,60,10,30,80,50,100]
l.sort()#ascending order
print(l)
l.sort(reverse=True)#decending order
print(l)'''
#xii)clear:
'''l=[1,2,3,4,5,6,7,8,9,10]
l.clear()
print(l)'''
#list comprehensions:
'''l=[x for x in range (1,11)]
print(l)'''
'''l1=[x**2 for x in range (1,11)]
print(l1)'''