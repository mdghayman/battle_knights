from knight import Knight
from item import Item

R = Knight([0,0], 'ALIVE', Null, 1, 1)
B = Knight([7,0], 'ALIVE', Null, 1, 1)
G = Knight([7,7], 'ALIVE', Null, 1, 1)
Y = Knight([0,7], 'ALIVE', Null, 1, 1)
knights = [R, B, G, Y]

A = Item(2, 0, 40, [2,2], No)
M = Item(1, 1, 30, [5,2], No)
D = Item(1, 0, 20, [2,5], No)
H = Item(0, 1, 10, [5,5], No)
items = [A, M, D, H]

def read_moves():
    moves = open('moves.txt').read().split('\n')[1:-2]
    moves = moves[moves.index('GAME-START'):moves.index('GAME-END')]

    turns = {}

    for i in range(len(moves)):
        turns[i] = [moves[i][0],

for i in range(len(moves)):
    turns[i] = Move(turn, move[0], move[2]

    move_names.append('turn'+str(i+1))
    holder = {move_names[i]: Move(move[0], move[2]) for name in move_names}

    turns.append()
