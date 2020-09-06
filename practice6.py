#Have the user enter a string and then determine whether it is a Palindrome

string1 = input("Enter a string: ").lower()
string2 = string1[::-1]

print(string1)
print(string2)

if string1 == string2:
	print('This is a Palindrome')