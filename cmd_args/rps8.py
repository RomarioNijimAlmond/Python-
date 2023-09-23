import sys
import random
from enum import Enum

def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # rock paper scissors

        player_choice = input(
            f"{name}, please enter ... \n 1 for rock, \n 2 for paper,\n or 3 for scissors:\n\n")

        #base_case
        if(player_choice not in ["1","2","3"]):
            print(f"{name}, invalid: you must enter a number from 1 to 3")
            return play_again()

        player = int(player_choice)
        if player < 1 or player > 3:
            sys.exit("invalid: you must enter a number from 1 to 3")

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        print("")
        print(f"you chose {str(RPS(player)).replace('RPS.','')} ")
        print(f"python chose {str(RPS(computer)).replace('RPS.','')}")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins

            if player == 2 and computer == 1:
                player_wins += 1
                return f"{name},you win"
            elif player == 1 and computer == 3:
                player_wins += 1
                return f"{name},you win"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name},you win"
            elif player == computer:
                return"tie game!"
            else:
                python_wins =+ 1
                return"python wins"
            
        game_result = decide_winner(player, computer) # values from the variables above the function decide_winner()
        
        print(game_result)
        
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")
        print("\nPlay again?")
        while True:      
            play_again = input("\nY for yes OR\nQ to quit \n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break

        if play_again.lower() == "y":
                return play_rps()
        else:
            print("thank you for playing")
            sys.exit("Bye!")

    return play_rps

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience!"
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the persion playing the game!."
    )

    args = parser.parse_args()


    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
