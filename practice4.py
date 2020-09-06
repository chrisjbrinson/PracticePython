#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides 
#evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input("Enter a number: "))
list1 = list(range(1,(num + 1)))

list2 = []

for element in list1:
	if num % element == 0:
		list2.append(element)

print(list2)