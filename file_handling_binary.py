# rb --> read binary
import os

with open(r"C:\Users\Gautam\Desktop\img_1.jpg", "rb") as file:
    data = file.read()
    print(data)
with open("new_img.jpg", "wb") as file:
    file.write(data)

# if you will use python to copy stuff it will be faster than your regular copy

# copy all files from a folder to another folder keep name of copied file same

def file_read():
    pass

def file_save():
    pass

# os.listdir()

# os.remove("new_img.jpg")

