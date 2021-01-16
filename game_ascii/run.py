from setup import knights, items

moves = open('moves.txt').read().split('\n')[1:-2]

for move in moves:
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
                total_attack = mover.attack (mover.item).attack + 0.5
                total_defence = defender.defence + (defender.item).defence
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

print(game_state)
