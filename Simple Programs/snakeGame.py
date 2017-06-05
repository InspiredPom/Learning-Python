import curses
from curses import KEY_RIGHT, KEY_LEFT,KEY_DOWN,KEY_UP
from random import randint

cellWidth = 40
cellHeight = 25

maxX = cellWidth - 2
maxY = cellHeight - 2
#Restricting snake,so it does not pass border

snakeLength = 5
snakeX = snakeLength + 1
#Snake head, the rest is body trailing behind it
snakeY = 3

timeOut= 100
#Speed

class Snake(object):
# def __init__(self):
#    self.x = 'Hello!'
#def method_a(self, foo):
#   print (self.x + " "  + foo)
#snake = Snake()
#snake.method_a("I am a snake")
    REV_DIR_MAP = {
        KEY_UP: KEY_DOWN, KEY_DOWN: KEY_UP,
        KEY_LEFT: KEY_RIGHT, KEY_RIGHT: KEY_LEFT,
    }

#Prevents head from hitting body when turning, by changing map direction accordingly
    def __init__(self, x, y, window):
        self.body_list = []
        self.hit_score = 0
        self.timeout = timeOut
        for i in range(snakeLength, 0, -1):
            self.body_list.append(Body(x - i, y))

        #Define and append the snakes head
        self.body_list.append(Body(x, y, '0'))
# define the window
        self.window = window
# Forces snake to right when game starts
        self.direction = KEY_RIGHT
# define where snake head coordinates
        self.last_head_coor = (x, y)
# define direction map
        self.direction_map = {
            KEY_UP: self.move_up,
            KEY_DOWN: self.move_down,
            KEY_LEFT: self.move_left,
            KEY_RIGHT: self.move_right
          }
    @property
#property - access later
    def score(self):
        return "Points : {}".format(self.hit_score)
#python format to pull score

class tail(object):
#  def __init__(self):
#    self.x = "This is the"
#  def method_a(self, foo):
#        print (self.x + ' ' + foo)
#body = tail().method_a('tail')
    def __init__(self, x, y, char='='):
        self.x = x
        self.y = y
        self.char = char
# modify function with special property decorator
    @property
# Set coordinate 
    def coor(self):
        return self.x, self.y


class fruit(object):
#def __init__(self):
#   self.y = 'Tastey '
#def method_a(self, foo):
#    print (self.y + ' ' + foo)
#fruit = fruit().method_a('Fruit')

#Initalize the Food
    def __init__(self, window, char='O'):
# choose random postion for food whenever its Initalized Boiiii
        self.x = randint(1, maxX)
        self.y = randint(1, maxY)
# here, we are just satifying the arguments, and setting the food character
        self.char = char
        self.window = window
# Make Render Function
    def render(self):
# This is using addstr, which is part of Curses Programing in Python
# this is adding food coordinates and character in string format 
        self.window.addstr(self.y, self.x, self.char)
#reset method, chooses new random coordinates when reset
    def reset(self):
        self.x = randint(1, maxX)
        self.y = randint(1, maxY)