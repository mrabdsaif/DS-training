from datetime import datetime

# print the currunt time and the task name ==> so we can compute the excution duration 
def print_time(task_name):
    print(task_name)
    print(datetime.now(), '\n')  # in the datetime library call the datetime object and then cal the now function of that object.
# first invoke :    
print_time('Task Begins')

for x in range(0,10):
    print(x)
# Second invoke 
print_time('Task completed')    

# a function returning people`s initials : (passing parameter into the function (name) the parameter are : fname and lname)
def get_initials(name):
    
    initials = name[0:1].upper()
    return initials
first_name = input('Enter Your First Name: ')    
last_name = input('Enter Your Last Name: ')
print(f'Your Initials are: {get_initials(first_name)}{get_initials(last_name)}')

