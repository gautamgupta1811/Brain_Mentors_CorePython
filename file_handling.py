import time
# something in which we have data
# types --> binary, text (.txt, .csv)
# files --> open, read, close
# types of operation --> read, write, append

# read file must exist

# ## file_name, mode
#
# file = open("myfile.txt", "r")
# file.seek(5)
# print(file.read(5))
# print("TELL", file.tell())
# print("="*25)
# print(file.read(10))
# print("Resetting seek")
# file.seek(0)
# print(file.read(10))
# file.close()


# # read, readline, readlines
# file = open("read_file.txt", "r")
# print("Output for read")
# print(file.read(5))
# print("Output for readline")
# print("First Line:", file.readline())
# print("Output for readlines")
# print(file.readlines())
# file.close()

# write --> file exist or not, write operation will create a new file

# file = open("sleep_and_add.txt", "w")
# # file.write("This data has been added for second time in this file")
# file.write("Before sleep")
# file.flush()
# print("Going for a sleep")
# time.sleep(20)
# print("Awaken again.. ")
# file.write("after sleep")
# file.close()

# file = open("file_writelines.txt", "w")
# data = ["firstline\n", "secondline\n"]
# file.writelines(data)
# file.close()

# append --> if file exist data is added to last else new created

# file = open("append_file.txt", "a")
# data = "this is some further data"
# file.write(data)
# file.close()

# r+, w+, a+

# file = open("read_write.txt", "w+")
# print("file variable", file)
# print("file read, sleeping now")
# # time.sleep(20)
# print("Executing again.. ")
# file.write("data")
# file.flush()
# print("Read data:", file.read())
# file.close()


with open('read_file.txt', 'r') as file:
    print(file.read())
print("Outside block")
# print(file.read()) --> error

# read from a file and save data into another file

