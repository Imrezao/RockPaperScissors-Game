# Rock-Paper-Scissors Game ✊✋✌️

A simple, interactive, and object-oriented command-line Rock-Paper-Scissors game written in Python. 

## 📝 Description

This project is a classic Rock-Paper-Scissors game where a user plays against the computer. The computer makes random choices, and the game evaluates the winner based on the standard rules. The user can play as many rounds as they want until they choose to exit.

The code is written with clean coding practices in mind, featuring **Object-Oriented Programming (OOP)**, strict **Type Hinting**.

## ✨ Features

- **Interactive Gameplay:** Play against the computer in the terminal.
- **Input Validation:** Automatically handles invalid inputs and prompts the user to try again.
- **Replayability:** Option to play multiple rounds without restarting the script.
- **Clean Code:** Fully annotated with Python Type Hints (`typing` module) and standard Docstrings.

## 🚀 How to Run

### Prerequisites
- **Python 3.6 or higher** (Required for Type Hints support).

### Execution
1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the game file (e.g., `main.py`).
4. Run the following command:
```bash
python main.py
```
### Example Usage
```
Enter your choice (rock/paper/scissors): rock
Computer choice: paper 
User choice: rock
Computer wins
Do u wanna play again? y/n
y
Enter your choice (rock/paper/scissors): scissors
Computer choice: paper 
User choice: scissors
User wins
Do u wanna play again? y/n
n
good bye
```
## 🏗️ Code Structure

The core of the game is built around the `RockPaperScissors` class, which contains the following methods:

- `__init__(choices, name)`: Initializes the game with valid moves and the player's name.
- `get_user_choice()`: Prompts the user for their move and validates it.
- `get_computer_choice()`: Randomly selects a valid move for the computer.
- `decide_winner(user_choice, computer_choice)`: Contains the logic to determine the winner of a round.
- `play()`: Orchestrates a single round of the game.

