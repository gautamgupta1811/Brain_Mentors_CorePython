file = open("append_file.txt", "r")
a = "hello"
while a:
    a = file.readline()
    print(a)
