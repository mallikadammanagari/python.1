#create otp using random method
'''import random 
otp=random.randint(100000,999999)
print("your OTP is:",otp)'''
#create otp using choices
from random import choices
digits = "0123456789"
otp = ''.join(choices(digits, k=6))
print("Your OTP is:", otp)





