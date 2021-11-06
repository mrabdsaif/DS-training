
### Working with files :
from pathlib import Path

cwd = Path.cwd()
demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# get the file name :
print(demo_file.name)
# get the extension :
print(demo_file.suffix)
# get the folder :
print(demo_file.parent.name)

# Get the size :
print('\n The file size is : \n ' + str(demo_file.stat().st_size) + '\n') # before we get the results for this, we need to check if the file exist




