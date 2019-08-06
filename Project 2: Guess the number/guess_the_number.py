# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

print "Guess The Number Game"
print "The Objective of the game is to guess the number selected by the computer in given range."

import random
import simplegui

# initialize global variables used in your code

n_range = 100
n_guess = 7
comp_number = 0
message = "Welcome!"

# define event handlers for control panel
def init():
    #funtion to initialize game
    global n_range, n_guess, comp_number, message
    comp_number = random.randrange(0,n_range)
    if n_range == 100:
       n_guess = 7
    elif n_range == 1000:
        n_guess = 10
    print "New Game"
    print "Range is 0 to", n_range
    print "Number of guesses remaining is", n_guess,"!"
    print " "
    message = "New Game!"

def range100():
    # button that changes range to range [0,100) and restarts
    global n_range, n_guess
    n_range = 100
    n_guess = 7
    init()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global n_range, n_guess
    n_range = 1000
    n_guess = 10
    init()

def get_input(guess):
    # main game logic goes here
    global n_guess, message
    guess_n = int (guess)
    print "Guess was", guess_n
    if comp_number < guess_n:
       n_guess = n_guess - 1
       if n_guess > 0:
          print "Number of guesses remaining is", n_guess, "!"
          print "Lower!"
          print ""
          message = "Lower!"
       else:
          print "Game Over!"
          print "The secret number was", comp_number
          print "Start again."
          print ""
          init()
    elif comp_number > guess_n:
         n_guess = n_guess - 1
         if n_guess > 0:
            print "Number of guesses remaining is", n_guess, "!"
            print "Higher!"
            print ""
            message = "Higher!"
         else:
            print "Game Over!"
            print "The secret number was", comp_number
            print "Start again."
            print ""
            init()
    else:
          print "Correct!"
          print ""
          init()

def draw(canvas):
    canvas.draw_text(message, [48,100], 24, "Red")

# create frame
fr = simplegui.create_frame("Guess The Number",200,200)

# register event handlers for control elements
fr.add_button("Range is [0,100)", range100, 200)
fr.add_button("Range is [0,1000)", range1000, 200)
fr.add_input("Enter a Guess", get_input, 200)
fr.set_draw_handler(draw)

# start frame
fr.start()
init()
