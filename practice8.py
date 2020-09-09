#Make a two-player Rock-Paper-Scissors game.

player1 = input("Player1 - Choose Rock, Paper, or Scissors: ").lower()
player2 = input ("Player2 - choose Rock, Paper, or Scissors: ").lower()

def compare(p1, p2):
	if p1 == p2:
		return("It's a TIE!!!")
	elif p1 == 'rock':
		if p2 == 'scissors':
			return("Rock wins!!!")
		else:
			return("Paper wins!!!")
	elif p1 == 'scissors':
		if p2 == 'paper':
			return("Scissors wins!!!")
		else:
			return("Rock wins!!!")
	elif p1 == 'paper':
		if p2 == 'rock':
			return("Paper wins!!!")
		else:
			return("Scissors win!!!")
	else:
		return("Try again")
		sys.exit()

print(compare(player1,player2))
