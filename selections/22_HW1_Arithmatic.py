# Homework 1: Arithmetic
# ● Read 2 integers A, B and print based on following cases:
# ○ if both are odd print their product A*B
# ○ if both are even print their division A/B (float division / assume B != 0)
# ○ if the first is odd and the second is even then find their sum A+B
# ○ if the first is even and the second is odd then find their subtraction A-B
# ● Inputs ⇒ outputs
# ○ 5 7 => 35
# ○ 12 2 => 6
# ○ 5 6 => 11
# ○ 12 3 => 9


A, B = map(int, input("Please enter number").split())
if A % 2 != 0 and B % 2 != 0:
    print(A * B)
elif A % 2 == 0 and B % 2 == 0:
    print(A/B)
elif A % 2 != 0 and B % 2 == 0:
    print(A + B)
else:
# if A % 2 == 0 and B % 2 != 0:
    print(A - B)
