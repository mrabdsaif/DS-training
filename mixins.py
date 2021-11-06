# Multiple inheritance (Mixins) :
# Every web developer at some pint has created some form of an application that is going to be a CURD app
# CRUD web application (create,retrieve,update,delete)
# rather than everytime we need to create one of those types of applications, let us instead use a code that somebody else has already created
# and one framework that has done that is called Django, and that allow me to integrate with it using mixins.
# Multiple inheritance : I am able to inherit from multiple classes 
# when to use mixins : either to take advantage of a framework or streamline something I am tryin to do the same thing over and over again 
# enable functionality for frameworks such as Django, streamline repetitious operations

# To better understand mixins, let`s highlight then this sceario :
# what I want to create : (I want to create my own framework) Helper database class 
# create different types for different databases
# what I want it to be able to do : (I will give you the ability to connect to a database) connecto to a database , log what it is doing
# And all what you need to do is only give me the name of the database that you want to connect to.
# Now, as you see above you just give me the name of the database and we do the rest for you so do not worry, and here where the mixins
# comes to play. 

class loggable: # to enable me logging the titles 
    def __init__(self):
        self.title = '' # Here we are looking for a title 
    def log(self):   # when find the title we are going to log it 
        print(f'Log msg from : {self.title}') # we are going to print it out into the screen 

class connection: # allow me to handle my connections 
    def __init__(self):
        self.server = ''
    def connect(self):
        print(f'Connecting database on server : {self.server}')

# Now If I am going to keep building this framework, how am I going to put this to action ?
# create our framework :
def framework(item): 
    #perform the connection :
    if isinstance(item,connection): # hey function framework, did you inherit from connection ?
       item.connect()   # if yes, now I can call the function connect.
    # lof the operation 
    if isinstance(item,loggable): # hey did you inherit from loggable ?
        item.log() # if you did, call log function 

# Now, I am going to create our database class 
# here we use the frame work, and inherit form conn. and loggable ...
class sqlDatabase(connection, loggable): # my database is going to inherit from connection and loggable classes 
    def __init__(self):
        super().__init__()
        # To enable all the appropriate the functionality is to set up those two properties to inherit from conn. and loggable 
        self.title = 'sql connection'
        self.server = 'some_server'
# for this class you are able to add whatever you want to add to do other functionality ...

# finally create an instance of this class 
sql_connection = sqlDatabase()
# Use our framework 
framework(sql_connection) # connects and logs 

# Note: the vast majority of using mixins is when you use an existing framework and the common thing is to use a framework that uses mixins.



# the great thing here is the fact that we can create brand new class, and this is going to be just logger 
    

class JustLog(loggable):
    def __init__(self):
        self.title = 'Just logging'
just_logger = JustLog()
framework(just_logger)

# and the same if you want to inherit from connection
class JustConnection(connection):
    def __init__(self):
        self.server = 'Just a server'
just_connection = JustConnection()
framework(just_connection)