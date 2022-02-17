
"""
Python Inheritance
inheritance allows us to define a class that inherits the methods and properties from another class

parent class -> Base class
Child class -> delivered class
class name must begin with a capital letter if they are more than one words use [CamelCase]
"""

#Create class person with last name and first name properties and print name method

#Parent Class
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def pname(self):
        print(f"My name is {self.lname} {self.fname}")


p1 = Person("Famba","Abdulnassiir")
p1.pname()

# Child Class
"""
To create a class that inherits the functionality from another class, send the parent class as a parameter 
when creating the child class:

Note "pass" key word is used when you don't want to leave the class empty and dont want to add any methods 
or properties to that class.
"""

class Student(Person):
    pass

p2 = Student("Natasha","Nabutanda")
p2.pname()

#Add __init__ to the child class for u to inherit from the parent also call person.__init__
class Student(Person):
    def __int__(self,fname,lname):
        Person.__init__(self,fname,lname)

# Super key word python also has super that is used to inherit methods from the parent
class Student(Person):
    def __int__(self,fname,lname):
        super().__init__(fname, lname)
        self.graduationyear = 2018 #Added a property called graudyationyear

