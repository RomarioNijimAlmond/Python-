import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

# rock paper scissors


def choose():
    player_choice = input(
        "enter ... \n 1 for rock, \n 2 for paper,\n or 3 for scissors:\n\n")

    player = int(player_choice)
    if player < 1 or player > 3:
        sys.exit("invalid: you must enter a number from 1 to 3")

    computer_choice = random.choice("123")
    computer = int(computer_choice)
    print("")
    print(f"you chose {str(RPS(player)).replace('RPS.','')} ")
    print(f"python chose {str(RPS(player)).replace('RPS.','')}")

    if player == 1 and computer == 2:
        print("python wins")
    elif player == 2 and computer == 1:
        print("you wins")
    elif player == 1 and computer == 3:
        print("you win")
    elif player == 3 and computer == 1:
        print("python wins")
    elif player == 2 and computer == 3:
        print("python wins")
    elif player == 3 and computer == 2:
        print("you win")
    elif player == computer:
        print("tie game!")
    else:
        print("python wins")


choose()
