from os import system
from time import sleep
from art import art
from setup import items
from states import board_state, game_state
from process import process
import json

# moves = open('moves.txt').read().split('\n')[1:-2]


# for item in items:
#     system('clear')
#     print('\nWELCOME TO BATTLE KNIGHTS!\n')
#     board_state()
#     print('\n')
#     for line in art()[item.code]:
#         print(line)
#         sleep(0.01)
#     sleep(1)

# turn = 1
# for move in moves:
#     process(move, turn)
#     turn = +1

# # After final turn, announce game over.
# print('\nGAME OVER!\n')

# with open('final_state.json', 'w') as f:

game_state = game_state()

final_state = '' + '{\n'
for key, value in game_state.items():
    final_state += f'    "{key}": {value},\n'
final_state += '}'

with open('final_state.json', 'w') as f:
    f.write(final_state)
