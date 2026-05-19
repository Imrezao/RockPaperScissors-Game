"""
Author: Reza Omidi
Date Created: 4/19/2025
Description: RockPaperScissor Game.
"""

import random
import sys
from typing import List, Tuple          


class RockPaperScissors:
    """
    Main class for RockPaperScissor Game.
    """
    def __init__(self,choices, name) -> None:
        self.choices: list[str] = choices
        self.name = name
        
    def get_user_choice(self) -> str:
        inpurt_map = {
            '1': 'rock', 'rock': 'rock',
            '2': 'paper', 'paper': 'paper',
            '3': 'Scissors', 'scissors': 'scissors'
        }
        while True:
            user_input: str = input('Enter your choice (q to quit):\n1-Rock \n2-Paper \n3-Scissors\n')
            if user_input.strip().lower() == 'q':
                print('Good Bye')
                sys.exit()

            if user_input.strip().lower() in inpurt_map:
                return user_input.lower()

            print('Invalid choice, try again')
            return self.get_user_choice()

    def get_computer_choice(self) -> str:
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        if user_choice == computer_choice :
            return 'It is a Tie'

        for item in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
            if user_choice == item[0] and computer_choice == item[1]:
                return 'User wins'
     
        return 'Computer wins'    


    def play(self) -> None:
        user_choice: str = self.get_user_choice()
        computer_choice: str = self.get_computer_choice()
        winner: str = self.decide_winner(user_choice, computer_choice)
        print(f"Computer choice: {computer_choice} \nUser choice: {user_choice}")
        print(winner)
        

if __name__ == '__main__':
    game = RockPaperScissors(['rock', 'paper', 'scissors'], 'Reza')

    while True:
        game.play()
        print('Do u wanna play again? y/n')
        if input().lower() == 'y':
            continue

        print('Good Bye')
        break
