# List is covered in [] and its better to add one type of data within the list

numbers = [1,2,3,4,-20,-1]
print(numbers) #prints all the items with in the list
print(numbers[2]) #access a particular item with in the list we can access it by calling its index

# Useful list Methods
#simply to access these methods put the list name followed by . after it a list of methods will be listed
numbers.sort() #sort items in the list
print(numbers)

print(len(numbers)) #print out the number of the items in the list

numbers.append(10) #Add to to the list it will be taken to last position in the list
print(numbers)

# numbers.clear() #clear all items from the list
print(numbers)

print(30 in numbers) #check if a certain number is with in the list

#there are many methods for working with list but these are the most common ones and to get the rest keep practicing
#and trying out code challenges on the net so u can encounter other methods.

#Deleting from List
print(numbers)

numbers.remove(2) #Removes that number put with in the method like it will remove the 1st 2
print(numbers)

numbers.pop() #deletes the last element at the top of the list (last number from right)
print(numbers)

del numbers[0] #delete number at index [x]
print(numbers)

del numbers[0:3] # this helps to delete a range of numbers thats to say from index 0 to 3 tho index 4 is excluded
print(numbers)