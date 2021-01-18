from os import system
from time import sleep
from setup import knights, items
from move_details import move_details
from states import board_state
from art import art

def process(move, turn):

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
