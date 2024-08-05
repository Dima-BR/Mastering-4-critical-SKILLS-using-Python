# Homework 2: Sort 3 numbers
# ● Given 3 integers, sort (order) them in ascending order and print them .
# ● Inputs ⇒ outputs
# ○ 1 23 ⇒ 123
# ○ 1 32 ⇒ 123
# ○ 2 13 ⇒ 123
# ○ 2 31 ⇒ 123
# ○ 3 12 ⇒ 123
# ○ 3 21 ⇒ 123
# ● Do you notice there are only 6 ways to permutate 3 numbers!

# if n1 <= n2 and n1 <= n3:
#     if n2 <= n3:
#         print(n1, n2, n3)
#     else:
#         print(n1, n3, n2)
# elif n2 <= n1 and n2<=n3:
#     if n1<= n3:
#         print(n2, n1, n3)
#     else:
#         print(n2, n3, n1)

a, b, c = map(int, input().split())

# To understand: apply on 3 2 1

if b < a:  # Swap them:
    a, b = b, a

# Now a and b are in correct order: e.g. 2 3 1

if c < b:  # Swap them
    b, c = c, b

    # Now b, are correct
    # But a, may not be again with b: e.g. 2 1 3

    if b < a:      # Swap them
        a, b = b, a

        # Now 1 2 3

print(a, b, c)
