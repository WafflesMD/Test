import datetime

name = input("Give me your name: ")
age = int(input("Enter your age: "))
ageleft = 100 - age

startyear = int(datetime.date.today().year)
print(startyear)
endyear = int(startyear + ageleft)
print(endyear)

print("Your name is " + name)
print("Your age is: " + str(age))
print("You will be 100 years old in " + str(endyear))