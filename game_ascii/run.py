from instances import knights, items
from art import art
from time import sleep
from os import system

art_cases = art()

board = [[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' '],
[' ',' ',' ',' ',' ',' ',' ',' ']]

def move_details(move):
    for knight in knights:
        if move[0] == knight.code:
            mover = knight
    direction = move[2]
    if mover.status == 'ALIVE':
        if direction == 'N':
            mover.position[0] -= 1
        if direction == 'S':
            mover.position[0] += 1
        if direction == 'W':
            mover.position[1] -= 1
        if direction == 'E':
            mover.position[1] += 1
        if mover.position[0] not in range(8) or mover.position[1] not in range(8):
            mover.status = 'DROWNED'
            mover.position = None
    for defender in knights:
        if defender != mover:
            if defender.position == mover.position:
                total_attack = mover.attack + 0.5
                for item in items:
                    if mover.item == item:
                        total_attack += item.attack
                total_defence = defender.defence
                for item in items:
                    if defender.item == item:
                        total_defence += item.defence
                if total_attack > total_defence:
                    defender.status = 'DEAD'
                else:
                    attacker.status = 'ALIVE'
    for loot in items:
        if loot.equipped == 'No':
            if loot.position == mover.position:
                if mover.item == None or mover.item.value < loot.value:
                    mover.item = loot
                    loot.equipped = True


def game_state():
    game_state = {}
    for knight in knights:
        game_state[knight.name] = [knight.position,
                                knight.status,
                                knight.item,
                                knight.attack,
                                knight.defence]
    for item in items:
        game_state[item.name] = [item.position,
                                item.equipped]
    print('{')
    sleep(.2)
    for key, value in game_state.items():
        print(f'"{key}":', value)
        sleep(.2)
    print('}')


def board_state():
    for item in items:
        board[item.position[0]][item.position[1]] = item.code

    for knight in knights:
        if knight.status == 'ALIVE':
            board[knight.position[0]][knight.position[1]] = knight.code

    for line in board:
        print('|'.join(line))


moves = open('moves.txt').read().split('\n')[1:-2]

turn = 1

print('\nWelcome to Battle Knights!')
sleep(.5)
print('\nStarting board:\n')
board_state()

for move in moves:
    sleep(2)
    system('clear')
    move_details(move)
    sleep(.5)
    print(f'\nTurn {str(turn)}:')
    sleep(.5)
    for key, value in art_cases.items():
        if move[0] == key:
            print(value)
            print(f'{move[0]} knight moves {move[2]}...\n')
    sleep(.5)
    board_state()
    turn += 1

sleep(.5)
print('\nGame over!\n')
