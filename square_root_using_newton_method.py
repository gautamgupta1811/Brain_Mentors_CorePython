num = int(input("Enter one number: "))
x = num
while True:
    root = 0.5 * (x + (num / x))
    if abs(root - x) < 0.00001:
        break
    else:
        x = root
print("Square root of {} is {}".format(num, root))
