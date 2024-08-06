# Homework 2: Find Maximum up to 10 numbers
# ● Read an integer N (1 <= N <= 10)
# ● Then read N numbers, find which of them has the biggest value and print it.
# ● Inputs (but they will be on seperate lines)
# ○ 5 1 3 2 4.5 2 ⇒ 4.5
# ■ 5 means read 5 integers
# ■ Then we read them [1 3 2 4.5 2]. Their maximum is 4.5 ○ 10167-988-4512990657734⇒129
# ●
# ■ Same as last homework. This time we are given first N (10)


cnt = int(input())

# read first number
result = float(input())
cnt -= 1

# read UP to 9 times
if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num

if cnt > 0:
    num = float(input())
    cnt -= 1
    if num > result:
        result = num


print(result)

