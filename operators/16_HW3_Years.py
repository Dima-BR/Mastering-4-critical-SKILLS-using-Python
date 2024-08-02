# Homework 2: Years!
# ● Assume a year is 12 months, but each month is 30 days ○ That is a year has 12 * 30 = 360 days
# ● Read an integer: whole number of days of someone age. Print 3 numbers
# ○ Total years total months remaining days 
# each 360 days a year
# each 30 days a month
# just days infant!
# Inputs ⇒ Outputs 
# 391 = 360 + 30 + 1 = 1 year, 1 month, 1 day 61 = 2*30 + 1
# 200 = 30*6 + 20
# 1000 = 2*360 + 9*30 + 10
# ○ 360
# ○ 30
# ○ 10
# ○ 391
# ○ 61
# ○ 200
# ○ 1000
# ○ 5000
# 10 0 01 0 0 0 10 11 1 02 1 0 6 20
# 2 9 10 13 10 20


days = int(input("please enter days.."))

y = days // 360
days = days % 360

months = days // 30
days = days % 30

print(y, months, days)
