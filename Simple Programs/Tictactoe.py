#Tic Tac Toe
#ToDo:Winner and Draw Results
import random
board = [0,1,2,
         3,4,5,
         6,7,8]

def show() :
  print(board[0],'|',board[1],'|',board[2])
  print ("--------")
  print(board[3],'|',board[4],'|',board[5])
  print ("--------")
  print(board[6],'|',board[7],'|',board[8])

winner = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],    # Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8],    # Vertical
    [0, 4, 8], [2, 4, 6]                # Diagonal
    ]

while winner is not None:
  spot = int(input("Enter a spot number: "))
  if board[spot] != 'x' and board[spot] != 'o':
    board[spot] = 'x'
      
    finding = True
    while finding:
        random.seed() 
        opponent = random.randint(0,8)
      #Generates a random spot for computer player
    
        if board[opponent] != 'o' and board[opponent] != 'x':
          board[opponent] = 'o'
          finding = False
  else:
    print("This spot is taken")
  print (show())
  print("\n")

  if winner == 'x':
    print ("Player 1 (X) wins!")
    break
  elif winner == 'o':
    print ("Player 2 (O) wins!")
    break
  elif winner == 0:
    print ("Game is a draw!")
    break