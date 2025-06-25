#print even numbers
mylist=[10,57,97,43]
even_number=[]

for i in mylist:
    if i %2==0:
       even_number.append(i)
print(even_number)