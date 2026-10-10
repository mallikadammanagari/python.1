'''import csv 
with open('students.csv','r')as f:
    students=csv.reader(f)
    for i in students:
        print(i)'''
#ex1:
'''import csv 
with open('students.csv','r')as f:
    students=csv.DictReader(f)
    for i in students:
        print(i)'''
#ex2:
import csv 
studentslist=[]
with open('students.csv','r')as f:
    students=csv.DictReader(f)
    for i in students:
        studentslist.append(i)
print(studentslist)
filtered_list=[]
for i in studentslist:
    d={}
    d.update({i['Student_ID']:i})
    filtered_list.append(d)
print(filtered_list)

