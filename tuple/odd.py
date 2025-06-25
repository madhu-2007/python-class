#odd
mytuple=(10,57,97,43)

odd_number=[]
for i in mytuple:
    if i %2!=0:
        odd_number.append(i)
print(odd_number)
print(tuple(odd_number)) 

