# Rock-Paper-Scissors Game

A simple, interactive, and object-oriented command-line Rock-Paper-Scissors game written in Python. 

## Description

This project is a classic Rock-Paper-Scissors game where a user plays against the computer. The computer makes random choices, and the game evaluates the winner based on the standard rules. The user can play as many rounds as they want until they choose to exit.

The code is written with clean coding practices in mind, featuring **Object-Oriented Programming (OOP)**, strict **Type Hinting**.


## Code Structure

- `RockPaperScissors`: The main controller class.

    - `__init__(choices, name)`: Initializes the game with valid moves and the player's name.
    - `get_user_choice()`: Handles internal mapping of inputs (1 ➔ rock), manages validation loops, and intercepts exit codes.
    - `get_computer_choice()`: Randomly selects a valid move for the computer.
    - `decide_winner(user_choice, computer_choice)`: Contains the logic to determine the winner of a round.
    - `play()`: Orchestrates a single round of the game.


## Prerequisites
- **Python 3.6 or higher** (Required for Type Hints support).
