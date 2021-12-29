# read (r), write(w) and append(a)

file = open("myfile.txt", "w+")
data = "Hello, adding some data to file"
file.write(data)
file.close()

file = open("myfile.txt", "r")
data = file.read()
print(data)
file.close()