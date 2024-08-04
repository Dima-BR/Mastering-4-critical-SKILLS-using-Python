# Last 3 digits!
# ● Read an integer and do the following:
# ○ If number < 10000, print this is a small number
# ○ Otherwise Sum the last 3 digits of the number
# ■ If the sum is odd, print this is a great number
# ■ Otherwise, If sum is even:
# ● If any digit of the last 3 digits is odd, print this is a good number
# ● Otherwise, print this is a bad number


n = int(input("enter number"))
if n < 10000: print("this is small number")
else:
    d1 = n%10
    n = n // 10
    d2 = n%10
    n = n // 10
    d3 = n % 10
    
    sum_last_3 = d1 + d2 + d3
    
    if sum_last_3 % 2 != 0: print("This is great number")
    else:
        is_d1_odd = d1 % 2 != 0
        is_d2_odd = d2 % 2 != 0
        is_d3_odd = d3 % 2 != 0
        
        if is_d1_odd or is_d2_odd or is_d3_odd:
            print("This is a good number")
        else: print("This is Bad Number")
