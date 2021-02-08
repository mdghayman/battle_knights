# Battle Knights

## Coding Challenge: Battling Knights

### Summary

* To execute a simple version of the game, and view the final output: run the file `MVP.py` (minimum viable product).
* To execute an ASCII art version of the game, with turn by turn illustration, and view the final output: run the file `run.py`.

### Introduction

This repository contains two versions of Battling Knights:
1. Simple game: A single file `MVP.py`, which uses the input file `moves.txt`. This final game state is output to the command line, and is also written to the file `final_state.json` which is then opened by the code.
2. ASCII art game: Several Python files, which are executed through the file `run.py`. This illustrates the game turn by turn, in the command line, with a diagram of the board and ASCII art of actions. The final game state is output to the command line, and is also written to the file `final_state.json` which is then opened by the code.

### Simple game

Only the file `MVP.py` is used for this version of the game.

### ASCII art game

The following files are used for this version of the game:
* `run.py`: Brings together the elements of the ASCII art game. Running this file will illustrate the game turn by turn in the command line, and output the final game to the command line, as well as saving it to the file `final_state.json` and then opening this file. It uses the file `moves.txt` to create a list of moves, executes the welcome function and then the process function for each move, and then generates the final game state.
* `setup.py`: Defines classes for knights and items, then creates each knight and item as instances of their respective classes, and then stores these objects in lists for easy reference.
* `states.py`: Creates two state templates: board state, which appears as an 8x8 board in the command line, with text symbols appearing to indicate the positions of any living knights and unequipped items; and game state, which creates a string in the JSON compatible format required as per the briefing, and showing the state of each knight and item.
* `art.py`: Contains a function createing a dictionary of drawings to illustrate each possible action in the game.
* `move_details.py`: Takes a text input of a given move, indicating the knight moving and the direction moved, and determines the resulting outcomes. Depending on the position moved to, these may include: moving to a new position on the board, or moving off the board and drowning; picking up an item, and dropping any less valuable items already held; and attacking a knight resulting on the defeat of either mover or defender.
* `process.py`: Defines a process function, to processes the outcomes of a given move, and illustrates the appropriate board state and ASCII art illustrations in the command line. Also defines a welcome function, to illustrate the start of the game with the initial board state and ASCII art of each item.
