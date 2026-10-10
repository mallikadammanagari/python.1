import random 
import string 
characters = string.ascii_letters + string.digits + string.punctuation
captcha=" "
for i in range (6):
    captcha+=random.choice(characters)
print(captcha)

