numbers = [10, 5, 9, 0,  2]

for i in range(len(numbers)):
    if numbers[i]%2!= 0:
        numbers[i]+=10

print(numbers)