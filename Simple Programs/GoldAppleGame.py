#ToDo: Get running
import time

#global gold
#global apples
gold = 90
apples = 0
def start():
  print ("Objective : Collect and Sell Apples\n")
  choice = input ("Do you want to play? Yes or no?")
  if choice == "Yes" or choice == "yes" or choice == "y":
    begin()
  if choice == "No" or choice == "no" or choice == "n":
    print ("That's Fine.Your choices matter ")
def begin():
	print ("Lets Begin")
	global gold
	global apples
	if gold > 99:
		print ("You Won")
		play = input("Do you want to play again?")
		if play == "Yes" or  play == "yes":
			apples = 0
			gold = 0
			begin()
		if play == "No" or play == "no":
		  print("Bye!")
	pick = input("Do you want to pick an apple?")
	if pick == "yes" or pick == "Yes":
		time.sleep(1)
		print("You picked an apple")
		apples = apples + 1
		print("You currently have ",apples, "apples")
	sell = input("Can I buy your apples?")
	if sell == "Yes" or sell == "yes":
		# gold
		#global apples
		print("You currently have", apples, "Apples")
		print("You sold your apples")
		gold += apples *10
		apples = 0
		print("You now have ", gold, "gold")
	begin()
start()