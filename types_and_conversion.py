# int, float, string

a = input("Enter first number: ")
b = input("Enter Second Number: ")
print(type(a))
a = int(a)
b = int(b)
print("sum of {} + {} is {}".format(a,b,a+b))

c = 23
print("String value of C is:",str(c))
print("float value of c is:", float(c))

print(int(True))
print(int(False))
print(True + True)

c = 23
print("Boolean of c is:",bool(c))
c = 0
print("Boolean of c is:",bool(c))
c = ""
print("Boolean of c is:",bool(c))
c = None
print("Boolean of c is:",bool(c))
c = -1
print("Boolean of c is:",bool(c))

c = "new string"
# c[0] = "w"

c = 10
d = c
print(id(c))
print(id(d))
