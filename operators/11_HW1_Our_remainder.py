# Homework 3: Our remainder
# ● We know N % M computes the remainder of division
# ● Write a program that reads 2 positive integers and print such reminder without
# using the modulus operator %
# ● Input: 27 12
# ● Output: 3
# ○ Remember in math: 27 % 12 = 3

n , m =map(int, input().split())

result = n-(n//m) * m

print(result)
