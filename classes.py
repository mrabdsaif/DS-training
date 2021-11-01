# Class is like an object constructor, or a blueprint for creating objects :
# To understand classes we need to understand that any class has a built in function called  __init__(), which is a function allows us to assign values
# to the properties of the object.
# The __init__() function is called automatically every time the class is being used to create new object.
# Classes define data structures and behavior.
# Why use classes : (Create reuseable components, group data and operations together)
# Classes are nouns ===> Properties are adjectives ===> methods are verbs
# The class name in python convension should be in PascalCasing 
# In the following class we have name and age that are available on the instance of this presenter object : 
# The class :
class Presenter:
  # The constructor : is where I am going to be able to create a new instance of this.
  def  __init__(self,name, age): # The different between the constructor and the normal function is when this is going to get called
                                 # This is going to get called when a brand new instance of presenter. (The first parameter is self)
                                 # self gives me access to the current instance of the object. after that we set up the whatever the parameter that I need are.
    # the following is called field and we defined name by using self, and name is availabe on the instance of this presenter obj.
     self.name = name
     self.age = age
     # In the following method we set up self so we can read all or our properties : 
  def say_hello(self):
      print('Hello ' + self.name + ' Your age is :' + str(self.age))

p1 = Presenter('Jhon',39)
p1.say_hello()

# When it comes to use it(the constructor), we can call the constructor much in the same way that we call a function
presenter = Presenter('Ali', 35)
presenter.name = 'Hani'  # You can update the name and the age on the fly 
presenter.say_hello()  # then I am able to say hello for that name 

# single underscore and douple underscore are used to control the accessibility to the property (fields & methods).
# (single underscore _ means) avoid this property or this method unless you know what are you doing. 
# (Couple underscore __ means) do not use this property (field) at all.

# To control a little bit better accessibility here, that we can limit what it is that somebody able to do to our class is by setting up 
# a property.
# What a propert is goingi to give to us is field style access, but actually using methods behind the scenes.
#  

class Presenter():
    # constructor
    def __init__(self,name):
       self.name = name # Here the constructor looks the same when declaring a field. but we just are calling the property (the setter).

    @property # Here, name is going to set up as a property. and the way to set up a property inside python is by creating getter side.
              # So if I said x = presenter.name it is going to give me this value back (that is mean the getter will be called)
    def name(self):
        print('In Ther getter')
        return self.__name  ## __ telling the outside world do not use this
             # Then we put the setter side where I put presenter.name = value like 'Ali'.
             # and the setter will be called when I say presenter.name = value 
    @name.setter
    def name(self,value):  # (We set this value into the field after checking it.
                           # what is happining here is the value this little 'Ali', will become part of the name.
                           # This gives me an opportunity to do a validation like checking if it is not empty string or null etc.
        print('In ther setter')
        # cool validation here
        self.__name = value  

presnter = Presenter('Ali') # creating an instance of the presenter
presenter.name = 'Hani'  # updating the value
print(presenter.name) # To finally print out the name



