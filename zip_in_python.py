names  = ["banana", "potato", "apple", "tomato", "strawberry"]
category = ["fruit", "vegetable", "fruit", "fruit", "fruit"]

'''for i in range(len(names)):
    print(names[i], category[i])'''

for i,j in zip(names, category):
    print(i, j)

for i, item in enumerate(names, 5):
    print(chr(65+i), item)


list_1 = eval(input("Enter elements of first vector: "))
list_2 = eval(input("Enter elements of second vector: "))

x = list_1[0] - list_2[0]
y = list_1[1] - list_2[1]
z = list_1[2] - list_2[2]

print((x**2 + y**2 + z**2)**0.5)

