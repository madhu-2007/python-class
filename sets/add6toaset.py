#add 6 to set
set={ 2,3,4,5,9}
set.add(6)
print(set)

#remove 3 from a set
set={2,4,3,5,6}
set.remove(3)
print(set)

#discard
set={2,3,5,6,8,9}
set.discard(6)
print(set) 

#create a string and print
string={"hello"}
print(string)

#check if 4 exist in a set
set={2,3,4,5,6}
if 4 in set:
    print("true")
else:
    print("false")    
#union
set1={1,2,3,4,5}
set2={3,4,5,6,7} 
y=set1.union(set2)
print(y)  

#intersection
set1={1,2,3,4,5}
set2={3,4,5,6,7}
y=set1.intersection(set2)
print(y)

#difference
set1={1,2,3,4,5}
set2={3,4,5,6,7}
y=set1.difference(set2)
print(y)

numbers=[1,2,3,4,5,6,6,5,4]
x=set(numbers)
print(x)

numbers={1,2,3,4,5,6}
print(len(numbers))

numbers={1,2,3,4,5}
for i in numbers:
  print(i**2,end=" ")

#vowels
x ={"a","e","i","w","r"}

for i in x:
    if i in ["a","e","i","o","u"]:
        print(i)


        





