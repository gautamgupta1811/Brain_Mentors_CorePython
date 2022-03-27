def add(x, y, z=0):
    return x + y + z


print(add(2, 3))
print(add(2, 3, 4))


def add_1(a, b):
    if type(a) is str:
        return a + b
    elif type(a) is int:
        return a + b


print(add_1(2, 3))
