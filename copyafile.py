# copyfile() = copies contents of a file
# copy() = copyfile + permission mode + destination can be a direcory
# copy2() copy() + copies metadata ( file's creation and modifcation times)

import shutil

shutil.copyfile('test.txt', 'copy.txt')
