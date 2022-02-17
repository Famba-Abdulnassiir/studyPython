"""
Python is OOP so almost everything in python is an object with properties
Here is were classes come into the pictures.
Classes are like blueprint of creating anything you can think of in the world (Objects)
Class -> object constractor or blueprint for creating objects

To create a class we use keyword
class MyClass:

Use the __init__() function to assign values to object properties, or other operations
that are necessary to do when the object is being created:
"""

#The __init__() Fucntion built in and always executed when the class is being initiated

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("Famba",27)

print(f"You are most welcome {p1.name} and your age is {p1.age}")

"""
Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object
"""

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # self parameter is a reference to the current instance of the class
    #and is used to access variables that belong to the class like here name and age
    def greet(self):
        print(f"Hello good morning {self.name}")

p1 = Person("Famba",27)

print(f"You are most welcome {p1.name} and your age is {p1.age}")
p1.greet()

#Modify object properties
p1.age = 30
print(p1.age)

#Delete Object Properties
del p1.age
print(p1.age) #it will through an error coze at this point age doesnt exist anymore deleted

#Delete and entire Object
del p1

#Pass keyword every class cant be left empty but were its inevitable u add pass keyword in the data area
class persson:
    pass #this is accepted u will see its use in the future when u have a class that u dont want to alter.