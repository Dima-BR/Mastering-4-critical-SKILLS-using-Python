# Homework 3: Maximum but constrained
# ● Given 3 integers, you have to find the biggest one of them which is < 100. ○ Print -1 if no such number
# ● Inputs
# ○ 22 90 115 ⇒ 90
# ■ Here [20 90] are only < 100. Maximum (20, 90) = 90
# ○ 200 300 400 ⇒ -1
# ■ All of them are > 100, so no answer
# ○ 50 100 150 ⇒ 50
# ■ Only 50 is < 100.
# ○ 10 30 20 ⇒ 30
# ■ The 3 numbers < 100, so their max is 30
# // my solution :)
a, b, c = map(int, input().split())

if a >= 100 and b >= 100 and c >= 100:
    ans = -1
else:
    ans = a 
    
    if ans < b < 100: ans = b
    if ans < c < 100: ans = c

print(ans)

# take a look on this https://github.com/Dima-BR/Mastering-4-critical-SKILLS-using-Python/blob/main/selections/operators/19_min_numbers.py 
