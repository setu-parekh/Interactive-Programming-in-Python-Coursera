# Mini Project 1: Rock-paper-scissors-lizard-Spock

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

def name_to_number(name):
    # Funtion Converts Name to corresponding number
    if name == "rock":
        return 0
    elif name =="Spock":
        return 1
    elif name =="paper":
        return 2
    elif name =="lizard":
        return 3
    elif name =="scissors":
        return 4
    else:
        print "Error : Invalid Name!"

def number_to_name(number):
    # Funtion Converts number to corresponding name
    if number == 0 :
        return "rock"
    elif number == 1 :
        return "Spock"
    elif number == 2 :
        return "paper"
    elif number == 3 :
        return "lizard"
    elif number == 4 :
        return "scissors"


def rpsls(name):
    # converting name to player_number using name_to_number
    player_number = name_to_number(name)
    # computing random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # computing difference of player_num and comp_number modulo five
    diff = ((player_number - comp_number)%5)
    # use if/elif/else to determine winner
    if diff == 0:
        winner = "Player and computer Tie!"
    elif (diff == 1) or (diff == 2):
        winner = "Player wins!"
    elif (diff == 3) or (diff == 4):
        winner = "Computer wins!"
    else:
        print "Error: Invalid Input"

    # converting comp_number to name using number_to_name
    computer_name = number_to_name(comp_number)
    # printing results
    print "Player chooses", name
    print "Computer chooses", computer_name
    print winner
    print "\n"


# testing code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
