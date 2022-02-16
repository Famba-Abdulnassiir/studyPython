
#They allow us to iterate through sets, lists, or dictionaries or any data structures in python.

# Loop through list tho it can also be a set
names = ["Famba"," Joan", "Habib", "Shadia"]
for name in names:
    print(name)

# loop through Dictionaries
person = {
    "name":"Famba",
    "age":"27",
    "address": "Canada"
}

for key in person:
    print(f"key: {key} value:{person[key]} ")

for key, value in person.items():
    print(key,value)

#Addition of numbers in a list
numbers =[1,2,5,6,7,8]
result = 0                   #this vairable was just created to store the result it was not in the question

for number in numbers:       #iterate thru numbers and add the result to them eg 0+1+2 etc
    result += number

print(result)

for i in range(10):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit)

for letter in "banana": #strings are also iteratable
    print(letter)