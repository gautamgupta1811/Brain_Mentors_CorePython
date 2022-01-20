import os
# relative and absolute path

# brain mentors --> rohini

# landmark --> 24/7

# folder --> localhites


with open("factorial.py") as file:  # relative path
    print(file.read())

with open(r"D:\Deceber\Core_Python\factorial.py") as file:  # absolute path
    print(file.read())


with open(r"../Deep_Learning/Mask_RCNN-master/Mask_RCNN-master/README.md") as file:  # relative path
    print(file.read())
# .--> current directory
print(os.path.isdir("."))

print(os.path.abspath("factorial.py"))

print(os.path.isfile("factorial.py"))


new_path = os.path.join(".", "factorial.py")
print(new_path)

