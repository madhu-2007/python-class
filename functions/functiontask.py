
# #1)check if a number is odd or even
# x=int(input("enter your number"))
# def myfunction():
#     if x%2==0:
#         print("x is even")
#     else:
#         print("x is odd")
# myfunction()

#2)comparing the two numbers and display the greatest number
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# def myfunction(a,b):
    
#     if a>b:
#         print(" a is greater ",a)
#     else:
#         print(" b is greater",b)
# myfunction(a,b) 

#3)to check if a given year is a leap year


# a =int(input("enter a year"))
# def year():  
#     if a%4 ==0 and a%400 ==0:
#         print("the given year is a leap year")
#     else:
#         print("the given year is not a leap year")  
# year()
# #1)check if a number is odd or even
# x=int(input("enter your number"))
# def myfunction():
#     if x%2==0:
#         print("x is even")
#     else:
#         print("x is odd")
# myfunction()
#4)find average

# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def avg():
    
#     average = sum(numbers) / len(numbers)
#     print(average) 
# avg()

    

#5) to check if a number is in the given range
# a=int(input("enter any number"))
# def myfunction(a):
   
#    if a>70 and a<100 :
#      print("the given number is in the range")
#    else:
#      print("the given number is not in the range")
# myfunction(a)


#6) print common elements from the list:

# list1=[5,6,7,8,9]
# list2= [7,8,9,11]
# def function(n1,n2):
#     common_elements = list(set(list1) & set(list2))
#     print(common_elements)
# function(list1,list2)

#7) squares
# def myfunction():
#     squares = []
#     for x in range(1, 11):
#         squares.append(x**2) 
#     print(squares)
# myfunction()


##8)determine the type of triangle based on its sides

# a = int(input("Enter the length of the side a: "))
# b = int(input("Enter the length of the side b: "))
# c = int(input("Enter the length of the side c: "))

# def triangle(a, b, c):
#     if a == b == c:
#         print("The given triangle is equilateral")
#     elif a == b or a == c or b == c:
#         print("The given triangle is isosceles")
#     else:
#         print("The given triangle is scalene")

# triangle(a, b, c)     

#9)print max from the list

# mylist=[10,20,50,5,90]
# def my_function(mylist):
#     maximum = mylist[0]
#     for i in mylist:
#         if i > maximum:
#             maximum = i
#     print(maximum)

# my_function(mylist)

#10)to check if a number is one or two digit
# a=int(input("enter your number"))
# def my_function(a):
#     if a>=1 and a<=9 :
#         print("the given number is positive one digit" )
#     elif a<=-1 and -9<=a:
#         print ("the given number is negative one digit")
#     elif a>=10 and a<100 :
#         print("the number is  positive two digit ")
#     elif a<=-10 and -99<=a:
#         print("the given number is negative two digit ")
#     else :
#         print("the given number is more than two digits ")
# my_function(a)


#11) my_list = [0, 1, 2, 4, 5, 6]

# def function():
#     count = 0
#     i = 0
#     while i < len(my_list):
#         if my_list[i] == i:
#             count += 1
#         i += 1  
#     print(count)

# function()

#12)to check if the given letter is a vowel or a consonant

# a=input("enter letter")
# def my_function():
#    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u"or a=="A" or a=="E" or a=="I" or a=="U" or a=="U":
#        print("vowel")
#    else:
#     print("constant")
# my_function()  

#13) numbers divisible by 3
# my_list = [2, 3, 4, 5, 6, 7, 7, 8, 9, 24]

# def function():
#     for i in my_list:
#         if i % 3 == 0:
#             print(i)

# function()




# #15)to print the grade with the percentage

# a=int(input("enter your percentage"))
# def function():
#  if a>=90:
#     print("grade A")
#  elif a>=80:
#     print("grade B")

#  elif a>=70:
#      print("grade C")

#  else:
#      print("grade D")
# function()

# def function():
    
#         if i % 3 == 0:
#           print(i)
# for i in range (1,101):
#      function()


##global scope

# msg="hello world!"
# def function():
#     print(msg,"inner")
# function()
# print(msg,"outer")

# a=[6,7,8,9,4]

# def my_function(b):
#     mylist=0
#     for i in b :
#         mylist+=i
#     print(mylist)
# my_function(a)
    