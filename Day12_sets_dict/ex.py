#checking whether set is a heterogeneous element or not?
'''s={1,23.1,'mallika',True,None,23+1j}
print(s)
print(type(s))'''
# lets check how many ways a set can be created ?
#ex 1:
'''string='python'
s1=set(string)
print(s1)'''
#ex 2: can we create a empty set or not
'''s1=set() #using set() we can create a empty set
print(type(s1))'''
#ex 3: traverse through set
'''s={1,2,3,4,5,6}
for i in s:
    print(i)'''
# methods of set
#i)issubset():checks whether all elements of one set is present in another set
'''s={1,2,5,7,8,9,10,15,20}
s1={1,2,10,15,20} 
print(s1.issubset(s))''' #smaller set contain bigger set
#ii)issuperset():checks whether set contain all elements of another set 
'''s={1,2,5,7,8,9,10,15,20}
s1={1,2,10,15,20} 
print(s.issuperset(s1)) #bigger set (s)contain smaller  set(s1)
'''
#iii)isdisjoint:checks whether two sets have no common element
'''s={1,2,3}
s1={4,5,6}
print(s.isdisjoint(s1))'''
#iv)copy():create a copy of an existing set
'''s={1,2,3,4,5}
s1=s.copy()
print(s1)'''
#v)add():add one element to a set
'''s={15,67,34,56}
s1=s.add(23)
print(s)'''
#vi)union():combines two sets and removes duplicates
'''s={1,2,3,4,5}
s1={3,5,7,8,9}
print(s.union(s1))'''
#vii)intersection():only common values available in both the sets
'''s={1,2,3,4,5}
s1={3,5,7,8,9}
print(s.intersection(s1))'''
#viii)differnce():
'''s={1,2,3,4,5}
s1={3,5,7,8,9}
print(s.difference(s1))
print(s1.differnce(s))
'''
#ix)symmetric_difference():removes common elements and prints all the elements
'''s={1,2,3,4,5}
s1={3,5,7,8,9}
print(s.symmetric_difference(s1))'''
#operators btw the sets
'''s1={1,2,3,4,5}
s2={4,5,8,9,10}
print(s1&s2)# AND performs intersection
print(s1|s2)#OR performs union 
print(s1-s2)# difference '''
#x)intersection_update:keep only the common elements and modifies the set
'''s1={1,2,3,4,5}
s2={4,5,8,9,10}
s1.intersection_update(s2)
print(s1)'''
#xi)difference_update:removes the common elements and prints remaining elements from one set .
'''s1={1,2,3,4,5}
s2={4,5,8,9,10}
s2.difference_update(s1)
print(s2)'''
#xii)symmetric_difference_update:removes common elements and prints remaining elements
'''s1={1,2,3,4,5}
s2={4,5,8,9,10}
s1.symmetric_difference_update(s2)
print(s1)'''
#xiii)discard():removes the particular value from the existing set
'''s1={1,2,3,4,5}
s1.discard(5)
print(s1)'''
#xiv)pop():
'''s1={1,2,3,4,5}
s2=s1.pop()
print(s2)
print(s1)'''
#xv)remove():
'''s1={1,2,3,4,5}
s1.remove(3)
print(s1)
'''
#xvi)update():
'''s1={1,2,3,4,5}
s2={6,7,4,5,9}
s1.update(s2)
print(s1)'''
#xvii)clear():
s={6,7,4,5,9}
s.clear()
print(s)
#Aggregate functions:
'''s={6,7,4,5,9}
print(sum(s))
print(max(s))
print(min(s))'''
#set comprehensions:
s1={x for x in range (1,11)}
print(s1)

