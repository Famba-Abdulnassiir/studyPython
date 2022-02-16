
#Dictionaries allows us to store key value pairs

person = {
    "name":"Famba",
    "age":27,
    "address":"Kampala"
}

print(person)
print(person["name"])
print(person["age"])
print(person["address"])
print(person.values()) #helps us to know the values
print(person.keys()) #helps us to know the keys to since we are dealing with keys and values

person["age"] = 28 # Change info with in the dictionary using its index (Keys) now age has been changed to 78.
print(person)