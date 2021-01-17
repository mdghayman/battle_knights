from setup import knights, items
from art import art

directions = {'N':[0,-1], 'S':[0,1], 'W':[1,-1], 'E':[1,1]}

def attack(mover, defender):
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
        attacker.status = 'DEAD'

def drown(mover):
    if mover.item is not None:
        drop = mover.item
        drop.holder = None
        drop.position = mover.position
    mover.status = 'DROWNED'
    mover.position = None

def pickup(mover, item):
    holding = mover.item
    if item.holder == None:
        if holding is None:
            item.holder = mover
            mover.item = item
        elif holding.value < item.value:
            item.holder = mover
            mover.item = item
            holding.position = mover.position
            holding.holder = None

def move_details(move):
    for knight in knights:
        if move[0] == knight.code:
            mover = knight
    direction = move[2]
    if mover.status == 'ALIVE':
        for key, value in directions.items():
            if direction == key:
                new_position = mover.position[value[0]] + value[1]
                if new_position in range(8):
                    mover.position[value[0]] = new_position
                else:
                    drown(mover)
            for item in items:
                if item.position == mover.position:
                    pickup(mover, item)
    for defender in knights:
        if defender != mover:
            if defender.position == mover.position:
                attack(mover, defender)
