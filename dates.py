# import datetime -> This works but it will form a long code and there is lot we are not using
from datetime import datetime
from datetime import date

# print(datetime.datetime.snow()) if we had imported datetime directly we had to call it all the time.
print(datetime.now())
print(datetime.now().date())
print(date.today())
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().day)
print(datetime.now().time)

"""
Working with dates is important because we are going to be using them prety much in the future.
they need attention but good enough python gat us covered with almost everything 
"""

# Fomart dates with python.
now = datetime.now()
print(now.strftime("%d %m %Y %H %M %S"))
print(now.strftime("%d/%m/%Y %H:%M:%S"))
print(now.strftime("%d-%m-%Y %H %M %S"))
print(now.strftime("%d-%B-%Y %H %M %S")) #when u want a month in full use capital B (Febrauary)
print(now.strftime("%d-%b-%Y %H %M %S")) #when you want to print abreav of the month use small b (Feb)

#you can choose to do it on the exact date method
print(datetime.now().date().strftime("%d-%B-%Y "))