# Homework 1: 100 or 7?
# ● Write a program that reads an integer and print 100 if number is even or 7 if
# number is odd
# ○ E.g. for input 8 ⇒ 100
# ○ E.g. for input 133 ⇒ 7

n = int(input("Please enter the number"))

even = n % 2 == 0

odd = not even

result = even * 100 + odd * 7 
print(result)
