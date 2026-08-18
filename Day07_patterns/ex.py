# # print a square of 5*5 '*'
# i=1
# while i<6:
#     j=1
#     while j<6:
#         if j<=i:
#             print('*',end=' ')
#         j+=1    
#     print()
#     i+=1
# #print a right angle triangle (method 1)
# i=1
# while i<6:
#    print(' *'*i)
#    i+=1

# #print a right angle triangle (method 2 )
# i=1
# while i<6:
#     j=1
#     while j<=6:
#         if j<=i:
#             print('* ',end='')
#         j+=1
#     print()
#     i+=1   
#print a right angle triangle for numbers using while loop
# i=1
# num=1
# while i<6:
#     j=1
    
#     while j<6:
#         if j<=i:
#             print(num ,end=' ')
#         j+=1
#     print()
#     num+=1
#     i+=1 
#  print a right angle using for loop 
# num=1
# for i in range(1,6):
#     for j in range (i):
#         print(num,end=' ')
#     num+=1
#     print()
#print a right angle using while loop for numbers 1 to 15
# i=1
# num=1
# while i<6:
#     j=1
#     while j<=i:
#         print(num,end=' ')
#         num+=1
#         j+=1
#     print()
#     i+=1
#print a right angle using for loop for number 1 to 15\
'''num=1
for i in range (1,6):
    for j in range (i):
        print(num,end=' ')
        num+=1
    print()'''
#print a right angle using while loop for a,b,c...o
'''i=1
ch=65
while i<5:
    j=1
    while j<i:
        print(chr(ch),end=' ')
        ch+=1
        j+=1
        
    print()
    i+=1
    '''
#print a right angle using * 
'''for i in range (1,5):
    for j in range (i):
      
        print('*',end=' ')
    print()'''
#print a square of 5*5
'''for i in range(5):
    for j in range (5):
        
            print('*',end=' ')
    print( )
            '''
#print reverse of right angle using while loop
'''i=1
while i<6:
    j=1
    while j<6:
        if j>=i:
            print('*',end=' ')
        j+=1
    print( )
    i+=1    '''
#print reverse of right angle using for loop 
'''for i in range (5,0,-1):
    for j in range (i):
        
            print('* ',end=' ')
    print( )    '''
#print pyramid using while loop
'''i=1
while i<6:
    print(' '*(5-i)+'* '*i)
    i+=1'''
print("Hello" * 3)