# This function will ask the user for their fname and lname and will return the first letters
# if you want your first letter to be in Uppercase you need to specify the second parameter True if not False.
def get_initial(name, force_uppercase):
    if force_uppercase:
        initials = name[0:1].upper()
    else:
        initials = name[0:1]
    return initials

# Here we ask the user to input their name
first_name = input('Enter Your First Name: ')
first_name_initial = get_initial(first_name,True)

last_name = input('Enter Your Last Name: ')
last_name_initial = get_initial(last_name,False)

# print statement to print out the initials of the user name 
print(f'Your Initials are : {first_name_initial}{last_name_initial}')


# This function contains parameters with defualt value for the second parameter (force_uppercase), so you do not need to specify it late.
# But if you want to change the defualt value you can specify your value later.
def get_initial_defualt_value(name, force_uppercase=True):
    if force_uppercase:
        initials = name[0:1].upper()
    else:
        initials = name[0:1]
    return initials

# Here we ask the user to input their name
first_name = input('Enter Your First Name: ')
first_name_initial = get_initial_defualt_value(first_name)

last_name = input('Enter Your Last Name: ')
last_name_initial = get_initial_defualt_value(last_name,False)

# print statement to print out the initials of the user name 
print(f'Your Initials are : {first_name_initial}{last_name_initial}')



# in this example we used named notation, i.e, when you call the function you specifiy the parameter with their values in any order you need
def get_initial_named_notation(name, force_uppercase):
    if force_uppercase:
        initials = name[0:1].upper()
    else:
        initials = name[0:1]
    return initials

# Here we ask the user to input their name
first_name = input('Enter Your First Name: ')
first_name_initial = get_initial_named_notation(force_uppercase=True,name=first_name)

last_name = input('Enter Your Last Name: ')
last_name_initial = get_initial_named_notation(name=last_name,force_uppercase=False)

# print statement to print out the initials of the user name 
print(f'Your Initials are : {first_name_initial}{last_name_initial}')

