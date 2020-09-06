#write a program that prints out all the elements of the list that are less than the number inputted by the user

list1 = [1,2,3,4,5,6,7,8,9]
list2 = []

number = int(input('Enter a number: '))

for element in list1:
	if element < number:
		list2.append(element)

print(list2)