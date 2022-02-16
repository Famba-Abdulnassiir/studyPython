
def greet():
    print("Hello Fans")

greet() #here we have invoked the function (function call)

"""
Function are to be much used in python and through out any programming language.
we have function declaration with 
 -> def functionName(parameters if any)
Please remember indentation is important here that's to say the code below the function is the what u 
want the function to execute [body of the function is just below the function]
"""

def user(name, password): #function declaration
    print(f"Welcome back {name} your password is {password}") #function body wat our function does

user("Famba","Fans!@3") #function call or invocation

#user with default values:

def usern(name="Fanspro",password="Fans!@"): #function declaration with default values
    if name == "Fanspro" and password == "Fans!@3":
        print(f"Your welcome {name}")
    else:
        print("Please check ure username or password")

usern()

"""
please note inorder to avoid errors at run time when the user dd not provide a value to some feild
its recommended in some feilds where default values can be assigned please do so.
"""

# Function return values
# Function that finds a person's gender
def convertGender(gender="unkown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return "unkown"

print(convertGender("M"))
print(convertGender("F"))
print(convertGender("m")) # make sure it works even when we use small letters coze diff users will use diff letters
print(convertGender("f"))
print(convertGender(""))