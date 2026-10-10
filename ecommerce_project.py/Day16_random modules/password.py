#create password uding random 
import random
import string
characters = string.ascii_letters + string.digits 
password = ""
for i in range(6):
    password+=random.choice(characters)
print("generated password:",password)

