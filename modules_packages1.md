#### Modules & Packages
## What is modules?
# A python file with functions, classes and other components.

### Why use modules ?
# Break code down into reusable structures & help make things a bit more readable.

### How to create a module ?
# It is pretty easy to create a module, only you can follow these steps :
* create a file with .py extention.
- example : 
#helpers.py
def display(msg,is_warrning=False):
    if is_warrning:
       print('This is a warining')
    print(msg)


# Now, when we need to use a module for different projects we need to import this module, and there are some ways to do that:
- import modules as namespace 
import helpers  (this line of code pulled in all the functions and make it available inside of a little collection or inside what is known as namespace called helpers, ie, the namespace=helpers)
helpers.display('')

- import all into current namespace 
from helpers import *  (this line of code to import every thing inside the module and you do not need to type in the namespace(helpers), and what that means every thing inside this module will be globally available or in a technical mannar it will then be imported into the current namespace, and the impact is when we want to access any function inside the module is just simply say the name of the function)
display('')

- import specific item (object) into current namespace
from helpers import display
display('')


# the previoues explanation was about a module we have created, now how about modules that others have created
# This is what we call [packages], so what is package :
* it is published collections of a modules 
* You can explore new packages through this site (python_packages_index)[https://pypi.org/]

# To install individual package you can use the powershell
pip install colorama

# If you happen to have a whole list of packages that you want to be able to install then the thing you can do is to set them up inside your txt file that is frequently known as requirement.txt 
pip install -r requirements.txt 

# requirements.txt
colorama

