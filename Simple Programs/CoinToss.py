import random
headcount = tailcount = 0
userinput = " "
print("Tossing a Coin")
while userinput.lower() != "q":
	flip = random.choice(["heads", "tails"])
	if flip == "heads":
		headcount +=1
		print("Heads", "The coin landed on heads", headcount, "time")
	else:
		tailcount+=1
		print("Tails", "The coin landed on tails", tailcount, "time")
		print ("press 'q' to quit")
		userinput = input("or another key to toss again")
	print ("Heads", headcount)
	print ("Tails", tailcount)