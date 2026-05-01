"""
Author: RezaOmidi
Date Created: 4/19/2026
Description: RockPaperScissor Game.
"""

import random
from typing import List, Tuple          

class RockPaperScissors:
    """main class for RockPaperScissor Game."""
    
    def __init__(self,choices, name):
        self.choices = choices
        self.name = name
        
    def get_user_input(self):
        # user_input = input('rock, paper, scissor:')
        # if user_input.lower() in self.choices:
        #         return user_input.lower()
        
        # print('invalid input, try again')
        # return self.get_user_input()

        while True:
            user_input: str = input('rock, paper, scissor:')
            if user_input.lower() in self.choices:
                return user_input.lower()
            
            
            print('invalid input, try again')
            # continue
            return self.get_user_input()

    def get_computer_input(self):
        return random.choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        if user_choice == computer_choice :
            return 'it is Tie'

        for item in [('rock', 'scissor'), ('paper', 'rock'), ('scissor', 'paper')]:
            if user_choice == item[0] and computer_choice == item[1]:
                return 'u won'

            
        return 'u lost'    


                
                

    def play(self):
        user_choice = self.get_user_input()
        computer_choice = self.get_computer_input()
        winner = self.decide_winner(user_choice, computer_choice)
        print(f"computer choice: {computer_choice} ### ur choice: {user_choice}")
        print(winner)
        

game = RockPaperScissors(['rock', 'paper', 'scissor'], 'reza')


if __name__ == '__main__':
    while True:
        game.play()
        print('do u wanna play again? y/n')

        if input() == "y":
            continue

        print('good bye')
        break

        
        
    