
# lots of decisions based on certain conditions this is where if statements comes in.

# Please note in python we use indentation which is : (semi clone) and we write else-if as elif

number = -12
if number > 0:
    print(f"number {number} is positive")
elif number == 0:
    print(number)
else:
    print(f"number {number} is negative")

"""
python tries as much as possible to make the code neat and very readable unlike other languages
as we discussed before indentation in python is very important with : or block of code below a certain line
elif for else-if

elif - allows us to take care of extra conditions in real life we can use it on scenarios
else - works at last when all the above conditions are not met.

Note we can only have one if and as many as we want elifs plus only one else incase the above elifs are not met
"""