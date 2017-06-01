import random

#rollAgain = "Yes"

#while rollAgain in ["Yes" , "yes", "y"]:
diceChoice = input ("Roll the Dice? Y/N")
if diceChoice in ["Yes" , "yes", "y", "Y"]:
    print("You rolled a ", random.randint(1,6))
    print("Thank you for playing")
else:
    print("Thank you for playing")

#TODO: Let user play again
