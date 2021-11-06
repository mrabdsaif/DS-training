####
from pathlib import Path

### Working with directories :
cwd = Path.cwd()
print('\n This is the current directory : \n' + str(cwd))

# Get the parent directory :
parent = cwd.parent

# Is this a directory :
print('\n Is this a directory : \n ' + str(parent.is_dir()))

# Is this a file ?
print('\n Is this a file : \n ' + str(parent.is_file()))


# List the child directories :
print('\n .....Directory Contents .... \n')
for child in parent.iterdir():
   if child.is_dir():
       print(child)


