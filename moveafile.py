import os

source = "test.txt"
destination = "/home/pkay7691/Projects/2023/4-23/python-practice/testfolder/test.txt"


try:
    if os.path.exists(destination):
        print("There is alreadya  file there")
    else: 
        os.replace(source, destination)
        print(source + "was moved")

except FileNotFoundError:
    print(source + " was not found")
