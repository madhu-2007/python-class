#replace all negatives with  zero
numbers = [-3, 5, -1, 0, 7, -8, ]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)