import random
Attempts = 0
num = random.randint(1, 10)
print("Guess a number between 1 and 10")

while Attempts < 3:
    
    guess = input()
    guess = int(guess)
    Attempts = Attempts + 1
    if guess < num:
        print("Too low.")
        print("Try Again?")
    if guess > num:
        print("Too high.")
        print("Try Again?")
    if guess == num:
        break
if guess == num:
  Attempts = str(Attempts)
  print("You are correct.")
if guess != num:
  num = str(num)
  print("Nope. The number was\n" + num)