import os
print(os.getcwd())


os.chdir("File Handling")
print(os.getcwd())

# file_obj = open("data.txt" , "r")
# content = file_obj.read()
# print(content)

# file_obj = open("data.txt" , "r")
# content = file_obj.readline()
# print(content)

# file_obj = open("data.txt" , "r")
# content = file_obj.readlines()
# print(content)

# file_obj = open("data.txt" , "rb")
# content = file_obj.read()
# print(content)

# file_obj = open("data.txt" , "w")
# file_obj.write("This is a new line.\n")
# file_obj.write("Appending another line.\n")
# print("Data written to file successfully.")
# file_obj.close()
# # content = file_obj.read()
# # print(content)
# file_obj = open("data.txt" , "w")
# file_obj.writelines("This is a new line.\n hi \ hello")

# print("Data written to file successfully.")
# file_obj.close()
# content = file_obj.read()
# print(content)



# file_obj = open("data2.txt", "x")
# print("new file created successfully.")

with open("data.csv","r") as file:
    content = file.read()
    print(content)
    file.close()

# with open("data.csv", "a") as file:
#     file.write("\n5, Ankit, 24")
#     print("data added successfully.")
#     file.close()    

