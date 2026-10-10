'''import random 
import string 
characters = string.ascii_letters + string.digits + string.punctuation
captcha=" "
for i in range (6):
    captcha+=random.choice(characters)
print(captcha)'''
#string
from random import randint,choices
import string 
s=string.ascii_letters
print(s)
randstr=choices(s,k=4)
print(randstr)
s1=string.digits
print(s1)