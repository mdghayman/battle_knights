from os import system
from time import sleep
from art import art
from setup import knights, items
from move_details import move_details
from states import board_state, game_state

moves = open('moves.txt').read().split('\n')[1:-2]
turn = 1


for item in items:
    system('clear')
    print('\nWELCOME TO BATTLE KNIGHTS!\n')
    board_state()
    print('\n')
    for line in art()[item.code]:
        print(line)
        sleep(0.01)
    sleep(1)


for move in moves:

    for knight in knights:
        if knight.code == move[0]:
            mover = knight
    direction_code = move[2]

    system('clear')
    outcomes = move_details(move)
    print(f'\nTURN {str(turn)}:\n')
    board_state()

    for key,value in {'N':'North','S':'South','E':'East','W':'West'}.items():
        if key == move[2]:
            bearing = value
    for key, value in art().items():
        if key == move[0] + move[2]:
            print(f'\n{mover.name} knight moves {bearing}.\n')
            for letter in value:
                sleep(0.01)
                print(letter)
            sleep(1)

    if 'drown' in outcomes:
        system('clear')
        print(f'\nTURN {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name} knight drowns!\n')
        for letter in art()['DROWNED']:
            sleep(0.01)
            print(letter)
        sleep(1)

    if 'pickup' in outcomes:
        item = mover.item
        system('clear')
        print(f'\nTURN {str(turn)}:\n')
        board_state()
        print(f'\n{mover.name} knight picks up {item.name}!\n')
        for letter in art()[item.code]:
            sleep(0.01)
            print(letter)
        sleep(1)

    for outcome in outcomes:
        if mover.name in outcome:
            system('clear')
            print(f'\nTURN {str(turn)}:\n')
            board_state()
            print(f'\n{outcome[1]} knight kills {outcome[0]} knight!\n')
            for letter in art()['DEAD']:
                sleep(0.01)
                print(letter)
            sleep(1)
        break

    turn += 1


system('clear')
print('\nGAME OVER!\n')
print('Final game state:\n')
game_state()
