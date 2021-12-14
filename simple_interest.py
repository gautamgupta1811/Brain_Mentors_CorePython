p = input("Enter Princpal Amount: ")
if not p.startswith("-"):
    if p.count(".") == 1:
        if len(p[p.index(".")+1:]) == 2:
            p = float(p)
            r = float(input("Enter rate of interest: "))
            t = float(input("Enter time period: "))
            print(p*r*t/100)
        else:
            print("Invalid P")
    elif p.count(".") == 0:
        p = float(p)
        r = float(input("Enter rate of interest: "))
        t = float(input("Enter time period: "))
        print(p*r*t/100)
    else:
        print("Invalid P")
else:
    print("Invalid P")
    
        

