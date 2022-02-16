
#Set is simillor to list but with set duplicates are not allowed.
"""
Rules to keep in mind while working with sets
    1.they use curry brackets {} unlike the list where we use []
    2.Sets donot allow duplicates
    3.the order is not guaranteed with sets
    4.have the same methods as the list
"""
numbersList =[1,1]
numbersSet = {1,1} # this set will only print 1 not 1 1
print(numbersList)
print(numbersSet)

letterSet = {"A","A","B","C","C"} # this set prints B A C here is were the rule of no order with sets is followed.
print(letterSet)

#Set Union Intersection and Difference.
# union uses symbol | (straight slash) it combines 2 sets into one

lettersA = {"A","B", "C"}
lettersB = {"D","C","E","F"}
union = lettersA | lettersB
intersection = lettersA & lettersB #only prints out the numbers that are same from A and B and we use & sign
differnce = lettersA - lettersB

print(f"union = {union}")
print(f"intersection = {intersection}")
print(f"Differnce {differnce}")

# Please remember the order does not matter with sets and its case sensitive if we have C and c it prints both


