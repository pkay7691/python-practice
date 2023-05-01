import os
import shutil


path = 'copy.txt'


try:
  # os.remove(path) delete a file
  # os.rmdir(path) dlete an empty directory
  # shutil.rmtree(path) delete a directory containing files (dangerous)
except FileNotFoundError:
  print("file was not found")
except PermissionError: 
  print("you do not have permission to delete that")
except OSError:
  print("You can not dlete that using that function")
else: 
  print(path + " was deleted")

