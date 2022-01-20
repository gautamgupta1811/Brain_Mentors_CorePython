import os

def save_file(file_name): #append_file.txt
    with open("../new_data/"+file_name, "wb") as file:  # ../new_data/append_file.txt
        file.write(read_file(file_name))


def read_file(file_name):  # append_file.txt
    with open(file_name, "rb") as file:
        data = file.read()
        return data


file_list = os.listdir()
for file in file_list:
    try:
        save_file(file)  # append_file.txt
    except:
        pass
