##for i in range(1,6,2):
##    print(i)

##name = "madhuvanthe"
##for n in name:
##    print(n)
##name=["apple","orange"]
##for i in name:
##    print(i)
##
##myList = [10,20,30,40]
##count = 0
##for i in myList:
##    count = count + i
##   
##print(count)
##
##for i in range(1,10):
##    if i == 5:
##        break
##    print(i)
##
##for i in range(1,10):
##    if i == 5:
##        continue
##    print(i)

# for i in range(1,10):
#     if i == 5:
#         print(i)
#         break
##      

    

##@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
##
##
##  print all numbers from 1-15
##for i in range (1,16):
## print(i)
##
## print odd numbers from 6-29
##for i in range (6,30):
## if i %2!=0:
##  print(i)
####print even numbers from 20-40
##for i in range(20,41):
##  if i%2==0:
##    print(i)
### print numbers divisible by 3 ,5 and both 3 and 5
# for i in range(1,16):
#  print(i)
#  if i%3==0 and i%5==0:
#    print("divisible by both 3 and 5")
#  elif i%3==0:
#     print("divisible by 3")
#  elif i%5==0:
#     print("divisible by 5")  
#  else:
#     print("divisible by none")
##
###print all elements of a list
##mylist=["apple","cherry"]
##for i in mylist:
##     print(i)
##     
##myList = [10,20,30,40]
##count = 0
##for i in myList:
##    count = count + i
##print(count)
##     
##
##count=0
##for i in  range(1,101):
##     count=count+i
##print(count)
##
## ###factorial values
##num = int(input("Enter a number: "))
##factorial = 1 
##if num < 0:
##    print("Factorial does not exist for negative numbers.")
##elif num == 0:
##    print("The factorial of 0 is 1.")
##else:
##    for i in range(1, num + 1):
##        factorial *= i
##print(factorial)
##
#fibanocci series
# n=int(input("enter any number"))
# a,b=0,1
# print("fibanocci series")
# for i in range(n):
#  print(a)
# a,b=b,a+b   

##numbers = [3, 5, 7, 2, 8, 1]
##max_number = numbers[0]  
##
##for i in numbers:
##    if i > max_number:
##        max_number = i
##
##print("The maximum number is:", max_number)

         

N = int(input("Enter a number: "))

# Initialize sum
sum_odd = 0

# Loop through numbers from 1 to N
for i in range(1, N + 1):
    if i % 2 != 0:
        sum_odd += i

# Print the result
print("Sum of odd numbers up to", N, "is:", sum_odd)





  
    
  

  
 
 





