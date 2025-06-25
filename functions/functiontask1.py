# #1)check if a number is odd or even
# x=int(input("enter your number"))
# def myfunction(x):
#     if x%2==0:
#        return  f"{x} is even"
#     else:
#        return  f"{x} is odd"
# print(myfunction(x))


# # 2)comparing the two numbers and display the greatest number
# a=int(input("enter your number"))
# b=int(input("enter your number"))
# def myfunction(a,b):
    
#     if a>b:
#         return  f"a is greater ",{a} 
#     else:
#         return f" b is greater",{b}
# print(myfunction(a,b))
 


# 3)to check if a given year is a leap year


# a =int(input("enter a year"))
# def year():  
#     if a%4 ==0 and a%400 ==0:
#        return f"the given year is a leap year",{a}
#     else:
#         return f"the given year is not a leap year" ,{a}
# print(year())

#4)check if a number is odd or even
# x=int(input("enter your number"))
# def myfunction(x):
#     if x%2==0:
#         return f"x is even"
#     else:
#         return f"x is odd"
# print((myfunction(x)))

# 5)find average

# numbers = [4, 15, 8, 23, 9, 2, 12, 7]
# def avg():
    
#     average = sum(numbers) / len(numbers)
#     return {average}
# print(avg())

#6) to check if a number is in the given range
# a=int(input("enter any number"))
# def myfunction(a):
   
#    if a>70 and a<100 :
#      return f"the given number is in the range"
#    else:
#      return f"the given number is not in the range"
# myfunction(a)

#7) print common elements from the list:

# list1=[5,6,7,8,9]
# list2= [7,8,9,11]
# def function(n1,n2):
#     common_elements = list(set(list1) & set(list2))
#     return f"{common_elements}"
# print(function(list1,list2))

#8) squares
# def myfunction():
#     squares = []
#     for x in range(1, 11):
#         squares.append(x**2)
#     return f"{squares}"

# print(myfunction())


#9)the type of triangle
# a = int(input("Enter the length of the side a: "))
# b = int(input("Enter the length of the side b: "))
# c = int(input("Enter the length of the side c: "))

# def triangle(a, b, c):
#     if a == b == c:
#         return f"The given triangle is equilateral"
#     elif a == b or a == c or b == c:
#         return f"The given triangle is isosceles"
#     else:
#         return f"The given triangle is scalene"

# print(triangle(a, b,c))    


##10)print max from the list



# mylist = [10, 50, 5, 90]

# def my_function(mylist):
#     maximum = mylist[0]
#     for i in mylist:
#         if i > maximum:
#             maximum = i
#     return{maximum}

# print(my_function(mylist))


#11)to check if a number is one or two digit
# a=int(input("enter your number"))
# def my_function(a):
#     if a>=1 and a<=9 :
#         return f"the given number is positive one digit"
#     elif a<=-1 and -9<=a:
#        return f"the given number is negative one digit"
#     elif a>=10 and a<100 :
#         return f"the number is  positive two digit "
#     elif a<=-10 and -99<=a:
#        return"the given number is negative two digit "
#     else :
#        return "the given number is more than two digits"
# print( my_function(a))


# 12) count how many elements are equal to their index

# my_list = [0, 1, 2, 4, 5, 6]
# def function():
#     count = 0
#     i = 0
#     while i < len(my_list):
#         if my_list[i] == i:
#             count += 1
#         i += 1  
#     return(count)

# print(function())

#13)to check if the given letter is a vowel or a consonant

# a=input("enter letter")
# def my_function():
#    if a=="a" or a=="e" or a=="i" or a=="o" or a=="u"or a=="A" or a=="E" or a=="I" or a=="U" or a=="U":
#      return f"vowel"
#    else:
#      return f"constant"
# print(my_function()) 

# numbers divisible by 3
# my_list = [2, 3, 4, 5, 6, 7,  8, 9, 24]
# result=[]

# def function():
#     for i in my_list:
#         if i % 3 == 0:
#             result.append(i)
#     return result

# print(function())
# # print(result)




# #15)to print the grade with the percentage

# a=int(input("enter your percentage"))
# def function():
#   if a>=90:
#      return f"grade A"
#   elif a>=80:
#      return f"grade B"
#   elif a>=70:
#      return f"grade C"
#   else:
#     return f"grade D"
# print(function())
