# Managing files :
# Working with files :
# The old way to manage your file was by using os.path
# Now in python 3.6 and higher, we use pathlib library to manage the files 
# Things we need to know about the files : what directory I am in ? what files are in that directory ?

from pathlib import Path 
# where am I ? cwd = current working directory 
cwd = Path.cwd()
print('\n Current Working Directory :\n ' + str(cwd))

# combine parts to create full path and file name : // creating full path name by joining path and file name 
new_file = Path.joinpath(cwd, 'new_file.txt') # Here we just create a file path and comine it with the directory name and file name
                                               # here we just create a file name this is why it returns False
print('\n Full Path is : \n ' + str(new_file))

# Does this exist ? // check if the file exist ?

print('\n Does This file exist : \n ' + str(new_file.exists()) + '\n')

