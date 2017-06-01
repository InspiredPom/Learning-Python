import random

user = input("Rock Paper or Scissors?")
computer = random.random()
if computer <=.33:
	computer = "Rock"
elif computer <= .66:
	computer = "Paper"
else:
	computer = "Scissors"

def game (first, second):
	if first == second:
		print ("You Chose", first)
		print ("Computer Chose", second)
		print ("You Tied")
	elif first == "rock":
		if second == "Scissors":
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Won!")
		else:
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Lost")
	elif first == "Paper":
		if second == "rock":
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Won!")
		else:
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Lost")
	elif first == "Scissors":
		if second == "paper":
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Won!")
		else:
			print ("You Chose", first)
			print ("Computer Chose", second)
			print ("You Lost")
game(user,computer)