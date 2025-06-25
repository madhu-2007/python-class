# thistuple = ("dog", "cat", "cow")
# print(thistuple) 

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple)

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(len(thistuple))

# tuple=("dog")
# print(type(tuple))
# tuple=("dog",)
# print(type(tuple))

# mytuple = ("apple", "banana", "cherry")
# print(type(mytuple))

# mytuple = ("apple", "banana", "cherry")
# print(mytuple[2])

# thistuple = ("apple", "banana", "cherry")
# print(thistuple[-1])

# thistuple = ("apple", "banana", "cherry", "apple", "cherry")
# print(thistuple[2:3])

# thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(thistuple[-4:-1])

# mytuple = ("apple", "banana", "cherry")
# if "apple" in mytuple : 
#     print("yes")



x = ("apple", "banana", "cherry")  
y = list(x)                        
y[1] = "kiwi"                     
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)   

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

###unpack tuples

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
for x in fruits:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1 

  x=("a","b","c")
  y=(1,2,3)
  z=x+y
  print(z)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5) 

print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

   