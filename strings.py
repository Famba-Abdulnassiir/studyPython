
#Generally here we shall look at the stings and there manuplations. diff methods applied to them
brand = "Fans Solutions Uganda"
print(brand.upper()) #Change to upper case
print(len(brand)) #check for the length of characters in the brand
print(brand.replace('a','u')) #replace an a in the brand with u
print(brand == "Fans Soln") #check if brand is same as "Fans soln"
print("Fans" in brand) #check if the word Fans is found with in the brand

#there are a number of methods that u may want to use simply make more practie with them
#simple add the variable name like brand. add a dot at the end u will see dropdown of different methods of strings.

#multline and formatting Strings
name = "Famba"

email = f"""
hello {name}
nice to meet you sir
hope ure this old{4+4}
"""

print(email)

#The above works in many situations but with long texts that u may need to edit
# or even not to aslong as u want them formated