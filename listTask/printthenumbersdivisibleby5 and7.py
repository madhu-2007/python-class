
# divisible_by_5 and 7 = [i for i in range(1, 101) if i % 5 == 0 and 1%7==0]
# print(divisible_by_5 and 7)

divisible=[]
for i in range(1,101):
    if i % 5 == 0 and i%7==0:
        divisible.append(i)
print(divisible)


