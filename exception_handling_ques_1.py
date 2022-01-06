# [1,2,3,4,5,6]

list_ = ["1", 2, "3", 4, "hello", "hi"]

prod = 1
for element in list_:
    try:
        prod *= int(element)
    except ValueError:
        pass

print(prod)
