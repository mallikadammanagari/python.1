import csv
customers=[]
with open('customers.csv','r')as f:
    reader = csv.reader(f)
    for i in reader:
        customers.append(i)
print(customers)       
