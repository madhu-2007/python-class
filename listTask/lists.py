#list task


#count positive and negative numbers
list=[10,-10,20,-20,30]
count_positive=0
count_negative=0
for i in list:
    if i>0:
        count_positive+=1
    elif i<0:
        count_negative+=1
print("number of positive number is :",count_positive)     
print("number of negative number is :",count_negative)


#print minimum from the list
mylist=[10,20,50,5,90]
print(min(mylist))




#reverse a list
list=[56,78,90,45,78]
print(list[::-1])

#print numbers divisible by 3
list=[3,24,97,78,54]
for i in list:
    if i%3==0:
      print(i)

#count how many times a number appears
list=[34,78,34,67,67,78]
target=67
print(list.count(target)) 

#remove all zeroes
list=[56,78,0,98,67]
list.remove(0)
print(list)

#replace all negatives with  zero
numbers = [-3, 5, -1, 0, 7, -8, 2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)
 
  
  #create a list of squares
 
   
squares = []
for x in range(1, 11):
    squares.append(x**2) 

print(squares) 

#find the second largest number
numbers=[6,7,8,9]
numbers.remove(max(numbers)) 
second_largest = max(numbers)  
print(second_largest)

#count how many elements are less tha 10
list=[9,8,12,43]
count=0
for num in list:
    if num < 10:
        count+=1
        print(count)

#find the average of a list
numbers = [4, 15, 8, 23, 9, 2, 12, 7]
average = sum(numbers) / len(numbers)
print(average) 


#print only duplicate elements :
list=[2,3,6,6,3,7]
result=[]
for i in list:
    if i not in result:
        result.append(i)
print(result)       

