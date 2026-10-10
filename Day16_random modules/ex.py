'''#1.random.random
import random
print(random.random())
#2.random.randint(a,b)
import random as r
print(r.randint(1000,9999))
#3.r.seed
import random as r
r.seed(13)
num=r.randint(1,10)
print(num)
#4.random.randrange
import random as r
num=r.randrange(1,20,2)
print(num)'''
#5.random.choice
'''import random as r
l=['red','green','oragne','yellow','black','blue']
print(r.choice(l))
#6.random.choices
import random as r
l=['red','green','oragne','yellow','black','blue']
print(r.choices(l,k=3))'''
#6.random.sample
'''import random as r
l=['red','green','oragne','yellow','black','blue']
print(r.sample(l,k=2))
'''
#7.random.shuffle
'''import random as r
l=['red','green','oragne','yellow','black','blue']
r.shuffle(l)
print(l)'''
