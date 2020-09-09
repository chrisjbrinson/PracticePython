#Generate a random number between 1 and 9 (including 1 and 9). 
#Ask the user to guess the number, then tell them whether they
#guessed too low, too high, or exactly right.

import random
guess = 0
counter = 1
number = random.randint(1,10)


while guess != number:
	guess = int(input("Please guess a number between 1 and 10: "))
	if guess < number:
		counter += 1
		finished = True
		print("Too Low")
	elif  guess > number:
		finished = True
		counter += 1
		print("Too High")
	else:
		print("You got it!")
		print("It only took you",counter,"times!!")
		exit()

