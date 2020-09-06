#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Give me your name: ")
age = int(input("How old are you?: "))

year = (100 - age) + 2020

print(name)
print("You will be 100yrs old in the year " + str(year))