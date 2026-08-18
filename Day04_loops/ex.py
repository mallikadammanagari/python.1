number=int(input('enter a number:'))

while number>0:
    res=number%10
    print(res)
    number//10
sum=0
while number>0:
    res=number%10
    sum+=res
    
    number//=10
print(sum) 
sum=0
for i in range (1,11):
    sum+=i

print(sum)