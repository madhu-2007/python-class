#counthowmanytimesanumberappears
numbers = (1, 2, 3, 4, 2, 2, 5, 1, 3)
target = 2 

count = 0
for num in numbers:
    if num == target:
        count += 1

print(f"The number {target} appears {count} times.")