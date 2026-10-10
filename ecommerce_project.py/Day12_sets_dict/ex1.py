'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d[1])
#using nested method
d=dict([[1,'one'],[2,'two'],[3,'three']])
print(d)'''
#using enumerate method
'''d1=dict(enumerate(['one','two','three','four','five'],start=1))
print(d1)
#using zip method
l1=[1,2,3,4,5]
l2=['one','two','three','four','five']
d3=dict(zip(l1,l2))
print(d3)
'''
#can we traverse through dict
#ex:1
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
for i in d:
    print(i) # only key'''
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
for i in d:
    print(d[i]) # only for values'''
#dictinary methods
#i)fromkeys:creates a new dictionary with the given keys and assigns the same value to all keys
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d.fromkeys([1,2,3,4,5]))'''
#ii)get:used to acces the value of a specified key 
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d.get(1))'''
#iii)keys():prints only keys from the existing dict
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d.keys())'''
#iv)values():prints only values from the existing dict
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d.values())'''
#v)items():prints items from the dict
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
print(d.items())'''
#vi)pop():removes any one element/any one item
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
d.pop(1)
print(d)'''
#vii)popitem():removes the last item
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
d.popitem()
print(d)'''
#viii)update():updating or modifing the exiting dictionary 
#ex:1
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
d.update({3:'three'})
print(d)
#ex 2:
d[4]='four'
print(d)
#ex 3:
d[1]='ace'
print(d)'''
#ix)clear():
'''d={1:'one',2:2,'data':[1,2,3,4,5,6]}
d.clear()
print(d)
#x)copy()
d={1:'one',2:2,'data':[1,2,3,4,5,6]}
d1=d.copy()
print(d1)'''
#dictionary comprehensions:
l=[(1,'one'),(2,'two'),(3,'three')]
d1={x:y for x,y in l}
print(d1)
#zip:
l1=[1,2,3]
l2=['one','two','three']
d2={x:y for x,y in zip(l1,l2)}
print(d2)
#enumerate:
l1=[1,2,3]
l2=['one','two','three']
d3={x:y for x,y in enumerate(l2,start=1)}
print(d3)