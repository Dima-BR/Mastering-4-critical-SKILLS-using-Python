# minimum of numbers 

# n1, n2 = map(int, input("please enter two numbers").split())
# if(n1<n2): print(n1)
# else: print(n2)

# min 3 numbers
# n1, n2, n3 = map(float, input("please enter 3 numbers..").split())
# if(n1<n2):
#     if(n1<n3):print(n1)
#     else: print(n3)
# elif(n2<n3): print(n2)
# else: print(n3)

# way2 //not the best way (if we have 10 numbers we should add 10 conditions !!!)
# num1, num2, num3 = map(float, input("enter 3 numbers.. ").split())
# if(num1 <= num2 && num1 <= num3): print(num1)
# elif(num2 <= num1 && num2 <= num3): print(num2)
# else: print(num3)

# Way 3 (best way to solve it) more scalable
no1, no2, no3 = map(float, input("enter 3 numbers.. ").split())
ans = no1
if(ans > no2): ans = no2
if(ans > no3): ans = no3

print(ans)
