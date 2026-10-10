#write mode
"""file=open('sample.txt','w')
print(file.writable())
file.write('''hi there!
how are you?
i am fine 
i am dng great
wt about
''')"""
#writelines
'''file=open('sample.txt','w')
file.writelines(['hi there!','\nhow are you','\nwelcome to python'])
file.close()'''
#readable
'''file = open("sample.txt", "r")
print(file.readable())
file.close()'''
#read
'''file = open("sample.txt", "r")
txt=file.read()
print(txt)
file.close()'''
'''file = open("sample.txt", "r")
txt=file.read(9)
print(txt)
file.close()'''
#readline:retun only first line
'''file = open("sample.txt", "r")
txt=file.readline()
print(txt)
file.close()'''
#readlines:returns whole data  in list format 
'''file = open("sample.txt", "r")
txt=file.readlines()
print(txt)
file.close()'''
#tell():
'''file = open("sample.txt", "r")
txt=file.readlines()
print(txt)
print(file.tell())#is used to find the current position of the cursor
file.close()'''
#seek():is used to move the cursor
'''file = open("sample.txt", "r")
print(file.tell())
file.seek(3)
txt=file.read()
print(txt)
file.close()'''

