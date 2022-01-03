# functions are used for avoidng repetation of code

def calc_simple_interest(p):  # formal parameter
    p = float(p)
    r = float(input("Enter rate of interest: "))
    t = int(input("Enter time period: "))
    print(p*r*t/100)

p = input("Enter principle amount: ")

if not p.startswith("-"):
    if p.count(".") == 1:
        if len(p[p.index(".")+1:]) == 2:
            calc_simple_interest(p)
        else:
            print("Invalid P")
    elif p.count(".") == 0:
        calc_simple_interest(p)  # actual parameter
    else:
        print("Invalid P")
else:
    print("Invalid P")
