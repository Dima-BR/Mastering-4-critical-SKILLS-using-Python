# Homework 2: Last 3 digits sum
# ● Write a program that reads an integer and prints the sum of its last 3 digits.
# ● Inputs ⇒ Outputs examples ○ 15 ⇒6
# ○ 125 ⇒8 ○ 1000 ⇒0 ○ 1001 ⇒1 ○ 1234 ⇒9 ○ 99999⇒27


n = int(input("Please enter the number"))

l1 = n%10
n = n // 10

l2 = n% 10
n //= 10

l3 = n%10
n //= 10 

result = l1 + l2 + l3
print(result)
