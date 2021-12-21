num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

if num_1 > num_2:
    a, b = num_1, num_2
else:
    a, b = num_2, num_1

r = 100

while r != 0:
    r = a%b
    a, b = b, r
print("GCD of {} and {} is {}".format(num_1, num_2, a))
