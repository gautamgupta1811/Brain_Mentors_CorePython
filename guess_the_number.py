import random

print("Think of a number between 1 to 100")
a = 1
b = 100
while True:
    c = random.randint(a, b)
    print("Guessed Number is: ", c)
    choice = input("Number is: ")
    if choice == "greater":
        b = c
    elif choice == "smaller":
        a = c
    else:
        print("Same number found")
        break
    
