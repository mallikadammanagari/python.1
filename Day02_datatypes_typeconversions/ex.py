#float
f=13.28
print(type(f),f) 
f1=1328e-2  # 10 can represent as e 
print(type(f1),f1)

#string
s='mallika'
s1="welocome to python"
s2=''' hello'''
print(type(s),s)
print(type(s1),s1)
print(type(s2),s2)

#boolean 
b=True
b1=False
print(type(b),b)
print(type(b1),b1)

#complex
c=13+28J # a complex numbers cannot be converted into int 
print(type(c),c)

#conversions
#conversion using int 
#string into int 

ss='58'
ss1='data science'
print(type(ss),ss)
a1=int(ss) # we can convert numbers into int 
print(type(ss1),ss1)
#a2=int(ss1) # we cannot convert the char string into int 

# float into int
 
x=20.05
y=int(x)
print(y) # we can convert a float into an int 
print(type(x),x)

#boolean into int 

b=True
a=int(b)
print(a)
print(type(b),b)

# conversion using string 
# int into string 
y=50
z=str(y)# we can convert a int to a string 
print(z)
print(type(y),y)

#float into string 
p=13.28
k=str(p)# we can convert a float into string 
print(k)
print(type(p),p)

#complex into string 
c=56+3j#we can covert a complex into string 
a=str(c)
print(a)
print(type(c),c)

#boolean into string 
a=False # we can convert a bool to string 
b=True # we can convert a bool to string 
c=str(a)
d=str(b)
print(c,d)
print(type(a),a)
print(type(b),b)

#conversion using float
#int into float
g=30
h=float(g)#we can convert a int to float 
print(h)
print(type(g),g)

#string into float 
s="200"# we can convert a string to float 
s1=float(s)
print(s1)
print(type(s),s)

#boolean into float 
b=True# we can convert a boolean to float 
a=float(b)
print(a)
print(type(b),b)

#complex into float 
#c=45+9j# we cannot covert a complex to float )

#coversion using boolean 
#int to boolean 
d=45#we can convert int to boolean 
d1=bool(d)
print(d1)
print(type(d),d)

#float to boolean 
f=34.65# we can convert float to boolean 
f1=bool(f)
print(f1)
print(type(f),f)

#string to boolean 
s="hello"#we can convert string to boolean
s1=bool(s)
print(s1)
print(type(s),s)

#complex to boolean 
c=34+4j# we can covert complex to boolean 
c1=bool(c)
print(c1)
print(type(c),c)

#conversion with complex 
#int to complex 
a=25#we can convert int to complex
a1=complex(a)
print(a1)
print(type(a),a)

#float to complex
f=23.23# we can convert float to complex
f1=complex(f)
print(f1)
print(type(f),f)

#string to complex 
s='python'#we cannot convert a char to complex 
#s1=complex(s)
#print(s)
print(type(s),s)
#
s=23#we can covert numbers to complex
s1=complex(s)
print(s)
print(type(s),s)

#boolean to complex
a=True
b=False
c=complex(a)
d=complex(b)
print(c)
print(d)
print(type(c),c)
print(type(d),d)
