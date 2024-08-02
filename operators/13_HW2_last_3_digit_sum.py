n = int(input("Please enter the number"))

l1 = n%10
n = n // 10

l2 = n% 10
n //= 10

l3 = n%10
n //= 10 

result = l1 + l2 + l3
print(result)
