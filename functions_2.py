def add(x, y):
    print(x + y)


def subtract(x, y):
    print(x - y)


def multiply(x, y):
    print(x * y)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = 45
add(a, b)
subtract(y=b, x=a)  # keyword arguments

def multiple_val(*args):
    print("inside multi_val function")
    for val in args:
        print(val)


multiple_val(a, b, c)

def default_arg_value(a, b, c=0):
    print(a)
    print(b)
    print(a + b)

default_arg_value(50, 34)

# def print(*value, sep=" ", end="\n")

def pass_keyword_arg(**kwargs):
    print(kwargs)

pass_keyword_arg(a="23", b=45)


# create  a function to accept user input values which can any number of values, find its sum

# create a a_m_counter to count occurence a and m in a string