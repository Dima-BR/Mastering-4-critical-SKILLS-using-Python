#  Find Maximum of 10 numbers
# ● Read 10 numbers and find which of them has the biggest value and print it.
# ● Inputs (each integer on a seperate line)
# ○1
# ○ 67
# ○ -9
# ○ 88
# ○ -45
# ○ 129
# ○ 90
# ○ 65
# ○ 77
# ○ 34
# ● Output ⇒ 129
# ● Restriction: In your whole code there should be 2 variables defined ONLY
# *** he input the numbers as float 

# Read first number
result = int(input())

# Read other 9 numbers
num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

num = int(input())
if result < num:
    result = num

print(result)
