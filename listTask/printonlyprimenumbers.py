#print prime numbers in a list
numbers=[3,4,5,6,7,8,27,31]
prime=[]
for num in numbers:
    if num >1:
        prime_is=True
        for i in range(2,num):
            if num%i==0:
                prime_is=False
                break
        if prime_is:
            prime.append(num)
print("prime numbers in the list:",prime) 



