n = int(input("enter number"))
if n % 2 == 0:
    print(n%10)
else:
    if n < 1000: print(n % 100)
    elif n > 1000 and n < 1000000: print(n % 10000)
    else: print(-n)
