#print the digits in a number
'''number=int(input('enter a number:'))'''
'''while number>0:
    result=number%10
    print(result)
    number//=10'''
#sum of the digits in a number 
'''sum=0
while number>0:
     res=number%10
     sum+=res
     number//=10
print(sum)'''
#how to traverse through string:
'''string='AchieversIT'
i=0
while i<len(string):
     print(string[i])
     i+=1'''
#palindrome of a number:
'''number=122
dup=number
reverse=0
while number>0:
     res=number%10
     reverse=reverse*10+res
     number//=10
if dup==reverse:
    print(dup,' is a palndrome')
else:
     print(dup,'is not a palandrome') 
     '''
#palindrome of string:
'''string='AchieversIT'
i=len(string)-1
rev=''
while i>=0:
    chr=string[i]
    rev+=chr
    i-=1
if string==rev:
    print(string,'is a palndrome')
else:
    print(string,'is not a palendrome')'''
#finding the factors of a number:
'''number=13
i=1
count=0
while i<=number:
    if number%i==0:
        print(i)
        count+=1
    i+=1
print('the factors of a number',number,'is :',count)
if count==2:
    print(number,'is a prime number')
else:
    print(number,'is not a prime number')  '''
#Task:
#print 1 to 100 using while loop
'''i=1
while i<101:
    print(i)
    i+=1
'''
#print 1 to 100 using for loop:
'''for i in range(1,101):
    print(i)'''
#print even or odd using while loop
'''i=1
while i<=50:
    if i%2==0:
        print(i,'is even')
    else:
        print(i,'is odd')
    i+=1'''
#print even or odd using for loop
'''for i in range (1,11):
    if i% 2==0:
        print(i,'is even')
    else:
        print(i,'is odd')'''
#print * instead of vowels using for loop 
'''name='mallika'
for str in name:
    if str in 'aeiouAEIOU':
        print('*',end='')
    else:
        print(str,end='')'''
#print * instead of vowels using while loop
'''name='mallika'
i=0
while i<len(name):
    if name[i]in 'aeiouAEIOU':
        print('*')
    else:
        print(name[i])
    i+=1'''
#print a prime number from 1 to 100
i=1
while i<=100:
    j=1
    count=0
    while j<=i:
        if i%j==0:
            count+=1
        j+=1
    if count==2:
        print(i,end=' ')
    i+=1