# Homework 1: Averages
# ● Write a program that reads 5 numbers and print the following:
# ○ A) Their average
# ○ B) The sum of the first 3 numbers divided by the sum of the last 2 numbers
# ○ C) The average of the first 3 numbers divided by the average of the last 2 numbers.
# ○ What is the math relation between B and C?
# ● Input 1 2 3 4 5 ○3
# ○ 0.666666667 ○ 0.444444444

n1, n2, n3, n4, n5 = map(float, input().split())
avg = (n1 + n2 + n3 + n4 + n5) / 5.0
B = (n1 + n2 + n3) / (n4 + n5)

C = ((n1 + n2 + n3)/3.0) / ((n4 + n5)/2.0)

print(avg, B, C)
print(B  * 2/3) #???
