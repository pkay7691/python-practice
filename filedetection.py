import os

path = '/home/pkay7691/Projects/2023/4-23/python-practice/exceptionhandling.py'

if os.path.exists(path): 
    print("This location exists")
    if os.path.isfile(path):
        print("that is a directory")
else:
    print("This location does not exist")
