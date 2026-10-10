'''l1=[[1,2,3],[4,5,6],[7,8,9]]
for i in l1:
    for j in i:
        print(j,end=' ')
    print()
'''
#using while loop:
'''l1=[[1,2,3],[4,5,6],[7,8,9]]
i=0
while i<len(l1):
    j=0
    while j<len(l1[i]):
        print(l1[i][j],end=' ')
        j+=1
    print()
    i+=1'''
#adding two martix:
'''l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
i=0
while i<len(l1):
    j=0
    while j<len(l1[i]):
        print(l1[i][j]+l2[i][j],end=' ')
        j+=1
    print()
    i+=1'''
#using append adding two list:
'''l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]]
l3=[]
i=0
while i<len(l1):
    j=0
    a=[]
    while j<len(l1[i]):
        x=l1[i][j]+l2[i][j]
        a.append(x)
        j+=1
    print()
    l3.append(a)
    i+=1
print(l3)'''
