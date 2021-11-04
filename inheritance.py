# What inheritance is, it is a generalization specialization
# what we do using inheritance is :
# Creates an 'is a' relationship (student is a person, (student is a specialization & person is a generalization))
# sqlconnectio is a Database connection, Nysqlconnection is a Database connection
## Composition (with property) creates a 'has a' relationship
# student has a class
# Database connection has a connectionstring 




# inheritance allows us to define a class (derived class) that inherits all the properties and methods from another class (parent class/base class)
print('Case 1:')
class Person:
    def __init__(self, fname, lname): # The parent constructor 
        self.fname = fname
        self.lname = lname
    def printname(self):
        print('Hello ' + self.fname , self.lname)

# Use the class to create a new object :
p1 = Person('Jhon', 'Doe')
# excute the print method :
p1.printname()
#print(p1.printname())

print()
print('Case 2 :')
# To create a class that inherits the functionality from the Person class, send the Person as a parameter when creating the child class
class Student(Person):
    # Now the childe class has the same properties and methods as the parent class.
    # Now you can create new object :
    pass # If the class is empty even if it is inheriting functionality from the parent we should add pass 
s1 = Student('Ali', 'Hani')
s1.printname()

# Now we need to add the __init__() function to the child class, this function is called automatically everytime the class is being used to
# create new object.
# When you add the __init__(), the child class is no longer inherits from the parent class.
# means that the child`s __init__ override the inheritance of the parent`s __init__().
# To keep the inheritance of the parent`s __init__ you need to add a call to the parent`s __init__ (Person.__init__(self...))
print()
print('Case 3 :')
class Student(Person):
    def __init__(self,fname,lname):  # Adding the __init__() to the child class 
        Person.__init__(self,fname,lname) # a call for the parent constructor to keep the inheritance
s2 = Student('Mohamed', 'Ahmad')
s2.printname()

# Now, To avoid using the name of the parent class as we use it to call the init function, we use the super().
# python has super(), allows the child class inherits the properties and the methods from its parent.
print()
print('Case 4:')
class Student(Person):
    def __init__(self,fname, lname, year): # u need to add the new parameter (year) so you can add the gradyear property.
        super().__init__(fname, lname) # using the super() u dont have to use the parent name to use the properties and the methods.
        self.graduationYear = year # To add new property to the class and you should pass it above in the init function.
s3 = Student('Fadi','Ahmad',2015) # you can create new object and add the gradyear 
s3.printname()
print(s3.graduationYear)

print() 
print('Case 5 :')
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationYear = year
    def welcome(self):
        print(f'Welcome {self.fname} {self.lname} to the class of {self.graduationYear}')

    def printname(self):
        # Let the parent do some work : 
        super().printname()
        # Add on custom code 
        print('I am rather tired')
    def __str__(self):
        return f'{self.fname} {self.lname} his grad year was in {self.graduationYear}'
s4 = Student('Abdullah','Saif',2021)
# when we run this statement the results it is not overly helpful, it is telling me that it is an object, it gives some memory address ...
           # and this is how python see the student s4, python does not know how to convert this into string
           # This is where str() comes in to play,__str__(self), and when you run this func you will get a helpful results for print(s4)
print(s4)    
print()
s4.printname()
s4.welcome()
print()
print(f'Is this(s4) a student ? {isinstance(s4,Student)}')
print(f'Is this(s3) a student ? {isinstance(s3,Student)}')

print(f'Is a this(s4) a Person ? {isinstance(s4,Person)}')

print(f'Is Student a Person ? {issubclass(Student,Person)}')


