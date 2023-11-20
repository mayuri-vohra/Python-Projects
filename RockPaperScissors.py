import random
player1=input('Select Rock, Paper, or Scissors :').lower()
print("Player 1 selected:",player1)
player2=randon.choice(['Rock','Paper','Scissors']).lower()
print("Player 2 selected:",player2)

if player1=='rock' and player2=='paper':
	print("Player 2 Won !")
elif player1=='paper' and player2=='scissors':
	print("Player 2 Won!")
elif player1=='scissors' and player2=='rock':
	print("Player 2 Won !")
elif player1==player2:
	print("It's A Tie !")
else:
	print("Player 1 Won !")