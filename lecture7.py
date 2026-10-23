# *****   File Input/Output in Python *******

# Python can be used to perform operations on a file. (read and write data)

# Types of all files
# 1. Text files: .txt, .docx, .log etc.]
# Binary Files: .mp4, .mov, .png, .jpeg etc.


# *******   Open, Read and closed file  *******

# we have to open a file before reading or writting.
# f = open("File_name", "made") 
# file_names = sample.txt or demo.docx ....so on and made = r:read mode or w:write mode

# data = f.read()
# f.close()

# Example
# f = open("pp.txt", "r")
# data = f.read()
# line1 = f.readline()
# print(data)
# print(type(data))
# f.close()

# Writing to file
# f = open("pp.txt", "w")
# f.write("Overwrites the entire file") # overwrites the entire file
# f.close()
# f = open("pp.txt", "a") # a is add at the end
# f.write("\nAppend the data with a") #adds to the file

# With Syntax

# with open("pp.txt", "r") as f :
#     data = f.read()
#     print(data)

# with open("pp.txt", "w") as f :
#     data = f.write("Through with WITH Syntax")
#     print(data)

# Deleting A File --------

# Using the os module
# Module (like a code library) is a file written by another
# programmer thet generally has a functions we can use

# import os
# os.remove("pp.txt")

# with open("Practice.txt", "w") as f:
#     f.write("Hi everyone\nwe are learning File I/O\n")
#     f.write("using Java\nI like programming in Java")
    
# with open("Practice.txt", "r") as f:
#     data = f.read()
# new_data =data.replace("Java", "Python")
# print(new_data)

# with open("Practice.txt", "w") as f:
#     f.write(new_data)
# srh_data = new_data.find(("learning"))
# print(srh_data)

# with open("Practice.txt", "r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("Found")
#     else:
#         print("Not Found")

def check_for_line():
    word = "Python"
    data = True
    line_no = 1
    with open("Practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
        
    return -1

# print(check_for_line())

def check_for_even():
   
    count = 0
    with open("Practice.txt", "r") as f:
        data = f.read()

        num = data.split(",")
        for val in num:
            if(int(val) % 2 == 0):
                count += 1
    print(count)

        


print(check_for_even())
