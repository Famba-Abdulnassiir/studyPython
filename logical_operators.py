
# Logical operators allows us to combine multiple expressions
# Please note in python we use keywords not like in other languages that we used symbols eg && here we use "and" word
# Note when u use and operator every expression has to evaluate to true for it to return true

print((10 > 5) and (1 > 3) and "A" == "C") #false because not all the expressions are true in the first place

# or Operator
#this returns true if any of the expressions is true
print((10 > 5) or (1 > 3) or"A" == "C")  #True since the first expression is true.

# not Operator #this returns true if the expression is not true
print(not("James" == "Maria")) # simply its true James is "not" Maria