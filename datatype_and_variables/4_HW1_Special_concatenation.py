# Homework #4: Special concatenation
# ● Write a program that read 3 strings.
# ○ For simplicity let’s say input is 3 letters A, B and C
# ● The output is A’B”C repeated 10 times
# ○ A’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”CA’B”C
# ● Input:
# ○ I
# ○ am
# ○ Mostafa
# ● Output:
# ○ I'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'am"MostafaI'a
# m"MostafaI'am"MostafaI'am"Mostafa

x = input("str 1")
y = input("str 2")
z = input("str 3")
concatStr = x + "'" + y + "\"" + z

print(concatStr * 10)
