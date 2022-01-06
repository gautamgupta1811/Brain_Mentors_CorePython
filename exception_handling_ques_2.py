def solve(exp):
    try:
        while len(exp) > 1:
            sub = exp[:3]
            print(sub)
            res = str(eval(sub))
            exp = res + exp[3:]
        print(exp)
    except IndexError:
        print("inside error")
        pass


solve("1+1*4-5")
