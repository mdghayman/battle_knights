from os import system
from time import sleep
from art import art
from setup import knights, items
from move_details import move_details
from states import board_state, game_state

for item in ['A','D','M','H']:
    system('clear')
    print('\nWELCOME TO BATTLE KNIGHTS!\n')
    board_state()
    print('\n')
    for line in art()[item]:
        print(line)
        sleep(0.02)
    sleep(1)

moves = open('moves.txt').read().split('\n')[1:-2]

turn = 1

for move in moves:
    for knight in knights:
        if knight.code == move[0]:
            mover = knight
    direction_code = move[2]
    system('clear')
    weapon_start = mover.item
    move_details(move)
    weapon_end = mover.item
    print(f'\nTURN {str(turn)}:\n')
    board_state()
    for key,value in {'N':'North','S':'South','E':'East','W':'West'}.items():
        if key == move[2]:
            bearing = value
    for key, value in art().items():
        if key == move[0] + move[2]:
            print(f'\n{mover.name.capitalize()} knight moves {bearing}.\n')
            for letter in value:
                sleep(0.02)
                print(letter)
            sleep(1)
    if mover.status == 'DROWNED':
        system('clear')
        print(f'\nTurn {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name.capitalize()} knight drowns!\n')
        for letter in art()['DROWNED']:
            sleep(0.02)
            print(letter)
        sleep(1)
    if weapon_start != weapon_end:
        system('clear')
        print(f'\nTurn {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name.capitalize()} knight picks up {weapon_end.name}!\n')
        for letter in art()[weapon_end.code]:
            sleep(0.02)
            print(letter)
        sleep(1)
    turn += 1

system('clear')
print('\nGAME OVER!\n')
print('Final game state:\n')
game_state()
