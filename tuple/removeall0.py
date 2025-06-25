
# tuple=(2,0,7,0,9,8)
# result=()

# for i in tuple:
#     if i !=0:
#       result.append(i)
# print(result)
#removeall0
mytuple = (2, 0, 7, 0, 9, 8)


result = tuple(i for i in mytuple if i != 0)


print(result)
