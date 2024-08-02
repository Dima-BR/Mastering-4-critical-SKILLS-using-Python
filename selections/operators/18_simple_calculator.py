n1, n2 = map(int, input("enter 2 numbers .. ").split())
s = input("Enter the sign ")

if(s == '+'):
    print(n1 + n2)

if(s == '-'):
    print(n1 - n2)

if(s == '*'):
    print(n1 * n2)

if(s == '/'):
    if(n2 != 0): print(n1 / n2)
    else: print("NA")
