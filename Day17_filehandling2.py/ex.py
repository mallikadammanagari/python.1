"""file=open('sample txt','w')
file.write('''hi there!
how are you ?
''')
file.close()"""
#append
"""file=open('sample txt','a')
file.write('''wt r u dng ?
ntg much 
wt abt u?
''')
file.close()"""
#with method
'''with open ('sample txt','r')as f:
    data=f.read()
    print(data)
print('retriving of data is completed')'''
#3.w+ #write+read mode
"""with open('sample.txt', 'w+') as f:
    f.write('''
hi there !
hello python ''')
    f.seek(0)
    print(f.tell())
    data = f.read()
    print(data)"""
#4 r+ #read+writemode
'''with open('sample txt','r+')as f:
    data=f.read()
    value=len(data)
    f.seek(value)
    f.write('\nhello world')'''
#5 a+ append+readmode
'''with open('sample txt','a+')as f:
    f.write('/nhow are you doing')
    f.seek(0)
    data=f.read()
    print(data)'''
#rb
'''data=None
with open('python.png','rb')as f:
    data=f.read()
    
#wb
with open('pythonclone.png','wb')as f:
    f.write(data)'''
    
