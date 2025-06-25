# 1)#emptydict
# thisDict={}
# print(thisDict)

# #2) create a dictionary with a new key value pair
# thisdict = {
#   "brand": "Ford",
#   "mobile": "876543219",
#   "age": 19
#   }
# print(thisdict)

# #3)access the value of key
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": 19
#   }
# 
# print(thisdict["age"])

# # #4) change the value of an existing key
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": 19
#   }
# thisdict["age"]=20

# print(thisdict["age"])

# #5)add a new key value pair
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": 19
#   }
# thisdict["class"]="12"
# print(thisdict)


#6) delete a key value pair
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }

# thisdict.pop("name")
# print(thisdict)

# # 7)check if a key value exists in dictionary
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }

# print("name" in thisdict)

# #8)print keys in dictionary
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }


# print(thisdict.keys())

# # 9)print values in dictionary
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }


# print(thisdict.values())

# # # 10)print key- values in dictionary
# # thisdict = {
# #   "name": "demo",
# #   "mobile": "876543219",
# #   "age": "19"
# #   }


# # print(thisdict.items())

# #11)merge two dict
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }
# dictionary={"class":12,
#              "date":"11,june"}  

# d=thisdict.update(dictionary)

# print(thisdict)

# # # 12)get the value
# # thisdict = {
# #   "name": "demo",
# #   "mobile": "876543219",
# #   "age": "19"
# #   }


# # print(thisdict.get("age"))

#13)loop through a dictionary
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }
# for x in thisdict:
#     print(x)



# # # 14)clear the dictionary
# # thisdict = {
# #   "name": "demo",
# #   "mobile": "876543219",
# #   "age": "19"
# #   }

# # print(thisdict.clear())
# # print(thisdict)

#15)nested dictionary
myfamily={"child1":{"name":"emily","year": 2007 },
          "child2":{"name":"olivia","year":"8"}}
print(myfamily)

#16)max key value pair
data = {
    "a": 15,
    "b": 42,
    "c": 8,
    "d": 29
}

# Initialize with first key-value pair
for k in data:
    max_key = k
    max_value = data[k]
    break

# Loop to find max value
for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Maximum value:", max_value)


# # 17)remove a key using pop
# thisdict = {
#   "name": "demo",
#   "mobile": "876543219",
#   "age": "19"
#   }



#18)## print(thisdict.pop("age"))
# print(thisdict)

#19)#sum all values in a dictionary
# thisdict={"a":6,"b":4,"c":8,"d":9}
# p=thisdict.values()
# print(sum(p))


# #check if all the values are even 
# thisdict={"a":6,"b":4,"c":8,"d":9}
# p=thisdict.values()

# for i in p:
#   if i %2==0:
#         print("the number is even " ,i)
#   else:
#         print("the number is odd" ,i) 


# #filter to keep elements above 50
# thisdict={"a":68,"b":46,"c":85,"d":39}
# p=thisdict.values()

# for i in p:
#   if i >=50:
#         print(i)
  
  

