# Homework 4: Conditional Count
# ● Write a program that reads number X, then other 5 numbers. Print 2 values:
# ○ How many numbers <= X
# ○ How many numbers > X
# ○ Any relation between these 2 outputs?
# ● Inputs
# ○ 10 300 1 5 100 200
# ○ Output: 2 3
# ○ Explantation
# ○ 2 numbers (1, 5) are <= 10
# ○ 3 numbers (100, 200, 300) are > 10

# first Sol
X, a, b, c, d, e = map(int, input().split())

countA = 0
countB = 0

if a > X:
    countA +=1
else:countB +=1
if b > X:
    countA +=1
else:countB +=1

if c > X:
    countA +=1
else:countB +=1

if d > X:
    countA +=1
else:countB +=1

if e > X:
    countA +=1
else:countB +=1


print(countA, countB)


# second Solution (without If )
x, a, b, c, d, e = map(int, input().split())

count = 0

count += a <= x
count += b <= x
count += c <= x
count += d <= x
count += e <= x

print(count, 5 - count)
