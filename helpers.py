# Here is an example of how to create modules and we will use it for the import modules and packages file & virtual enviornment file as well
from pip._vendor.colorama import init, Fore
def display(msg, is_warning=False):
    if is_warning:
        print(Fore.RED + msg)
    else:
        print(Fore.GREEN + msg)
