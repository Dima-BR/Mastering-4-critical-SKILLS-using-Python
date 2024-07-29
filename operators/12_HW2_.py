# Homework 1: Is even?
# ● The following code, reads an integer and computes a boolean if the number is even in 3 different ways. The number can be +ve or -ve.
# ● Fill in the is_even to solve the problem in 3 ways as following
# ● Using only %2
# ● Using only %10
# ● Using only /2

n = int(input("Please enter the number"))

is_even1 = n %2 == 0 

is_even2 = ((n / 2.0) - int(n / 2.0)) == 0
print(n / 2.0)
print(int(n / 2.0))

last_digit = n % 10 
is_even3 = last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

print(is_even1, is_even2, is_even3)
