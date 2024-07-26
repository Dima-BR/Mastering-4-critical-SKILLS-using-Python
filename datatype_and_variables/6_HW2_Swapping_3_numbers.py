# Homework 1: Swapping 3 numbers!
# ● Write a code to swap 3 numbers
# ● Let say we have numbers a = 115, b = 20, c = 301
# ● We wanna their final values to be: a = 20, b = 301, c = 115

a, b, c = map(int, input().split())

num4 = a
a = b
b= c
c= num4

print(a, b, c)
