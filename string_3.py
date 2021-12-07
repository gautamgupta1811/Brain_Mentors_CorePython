a = "python is high level programming language"

print(a.center(100))
print(a.center(100, "+"))

a = "hello"
b = "world"
print(a+" "+b)
print(a*5)

age = input("Enter age: ")
s1 = "Age of user " + age
print(s1)

s2 = "Age of user {}".format(age)
print(s2)

a = 10
b = 20
c = a + b

# sum of a and b is a+b

print("sum of  {} and {} is {}".format(a, b, c))
# formatted string
print(f"sum of {a} and {b} is {c}")
# %d, %f, %s

print("sum of %f and %f is %f"%(a,b,c))

# special characters \
# \n --> new line
print("Hello\nworld")
# \t --> tab
print("Hello\tworld")
# hello\nworld
print("Hello\\nworld")

# raw string
print(r"C:\Users\Gautam\Desktop\New Folder")

"Ram's sister"
"Ram's sister name is \"Ankita\""
print("""
hello this is python programming
  my name is gautam gupta
I am from Delhi
""")

