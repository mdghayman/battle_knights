from setup import knights, items
from art import art


def move_details(move):

    outcomes = []
    directions = {'N':[0,-1], 'S':[0,1], 'W':[1,-1], 'E':[1,1]}

    for knight in knights:
        if move[0] == knight.code:
            mover = knight
    direction = move[2]
    holding = mover.item

    if mover.status == 'ALIVE':
        for key, value in directions.items():
            if direction == key:
                position_shift = mover.position[value[0]] + value[1]
                if position_shift in range(8):
                    mover.position[value[0]] = position_shift

                    for item in items:
                        if item != holding:
                            if item.position == mover.position:

                                if holding is None:
                                    item.holder = mover
                                    mover.item = item

                                elif holding.value < item.value:
                                    item.holder = mover
                                    mover.item = item
                                    holding.holder = None
                                    holding.position = list(mover.position)

                                outcomes.append('pickup')

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
                                    defender.item = None
                                    outcomes.append([defender.name, mover.name])

                                else:
                                    mover.status = 'DEAD'
                                    mover.item = None
                                    outcomes.append([mover.name, defender.name])

                else:
                    if mover.item is not None:
                        drop = mover.item
                        drop.holder = None
                        drop.position = list(mover.position)
                    mover.status = 'DROWNED'
                    mover.position = None
                    mover.item = None
                    outcomes.append('drown')

    return outcomes
