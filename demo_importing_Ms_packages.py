# importing modules that I have created by importing just the module

#import helpers
#helpers.display('Sample msg', True)

# importing the item inside the module

from helpers import display
display('Sample msg',True)
from helpers import display
display('Sample msg',False)

# Now To create a virtual env (python -m venv venv) this will be installing to the vs code and then you need to activate it to be
# into your workspace using the powershell  