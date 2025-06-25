# to calculate square of a number
# square=lambda a: a**2
# print(square(6))

#to check if the number is even
# evennumber = lambda a: a%2==0
# print(evennumber(13))

#add 5 to all the numbers in the list
# numbers=[1,2,3,4,5,6,7,8]
# result=map(lambda x: x+5, numbers)
# print(result)
# print(list(result))

# to filter all the even numbers
# numbers=[1,2,3,4,5,6,7,8,9,10]
# def is_even(num):
#     return num%2==0
# even_numbers=filter(is_even,numbers)
# even_numbers_list=list(even_numbers)
# print(even_numbers_list)

# to calculate square
# numbers=[1,2,3,4,5,6,7,8,9]
# result=map(lambda x: x*x ,numbers)
# print(result)
# print(list(result))

# to filter even and odd numbers from the list
# numbers=[1,2,3,4,5,6,7,8,9,10] 

# def is_even(num):
#     return num%2==0

# def is_odd(num):
#     return num%2!=0

# even_numbers=filter(is_even,numbers)
# even_numbers_list=list(even_numbers)
# print(even_numbers_list ,"these numbers are even")


# odd_numbers=filter(is_odd,numbers)
# odd_numbers_list=list(odd_numbers)
# print(odd_numbers_list ,"these numbers are odd")

# convert the words into uppercase
# words=["hello","demo","world"]
# uppercase_words=list(map(lambda word: word.upper(),words))
# print(uppercase_words)

# to filter only the words starting with "s"
# my_list=["sun","moon","star","sky"]
# def words(a):
#     return a.startswith("s")

# word =filter( words ,my_list)
# words_list=list(word)
# print(words_list)  

# to convert the string numbers into integers
# string_numbers = ["5", "12", "100", "23", "45"]

# int_numbers = list(map(lambda x: int(x), string_numbers))

# print(int_numbers)


# to calculate the len of the words
# my_list=["demo","world","hellohi"]
# word=list(map(lambda x: len(x),my_list))
# print(word)

# to capitalize the words
# words=["hello","demo","world"]
# capitalize_word=list(map(lambda word: word.capitalize(),words))
# print(capitalize_word)


# to reverse the words
# words = ["hello", "demo", "world"]
# reverse_word = list(map(lambda word: word[::-1], words))
# print(reverse_word)

# to filters the word with more than tree letters
# my_list=["sun","moon","star","sky"]
# def words(a):
#     return len(a)>3

# word =filter( words ,my_list)
# words_list=list(word)
# print(words_list)
  
# to filter and print words from my_list other than empty string
# my_list=["sun","moon","star","sky",""]
# def words(a):
#     return a!=""

# word =filter( words ,my_list)
# words_list=list(word)
# print(words_list)  

# to filter only ppositive number
# my_list=[1,2,3,4,-1,-6,6,-7]
# def words(a):
#     return a>=0

# word =filter( words ,my_list)
# words_list=list(word)
# print(words_list)  


#to sort the second elements of the list
# my_list =[(1,2),(3,1),(5,0)]
# my_list.sort(key=lambda x: x[1])
# print(my_list)
 
# ##to find product of all the elements of a list
# mylist=[2,3,4,5,6,7,8]
# def product(x):


#to add the list element wise
# mylist = [1,2,3,4,5]
# my_list=[1,2,3,4,5]
# sum = list(map(lambda x,y: x+y, mylist,my_list))
# print(sum)

#to print all the elements that starts with a
# mylist=["anger","apple","orange","awesome","olive"]
# def lil(x):
#     return x.startswith("a")
# word=list(filter(lil,mylist))
# print(word)

    

###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# number=5
# result=factorial(number)
# print (f"the factorial of{number}:{result}")