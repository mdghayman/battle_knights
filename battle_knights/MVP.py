class Knight:
    def __init__(self, code, name, position, status, item, attack, defence):
        self.code = code
        self.name = name
        self.position = position
        self.status = status
        self.item = item
        self.attack = attack
        self.defence = defence

R = Knight('R', 'red', [0,0], 'ALIVE', None, 1, 1)
B = Knight('B', 'blue', [7,0], 'ALIVE', None, 1, 1)
G = Knight('G', 'green', [7,7], 'ALIVE', None, 1, 1)
Y = Knight('Y', 'yellow', [0,7], 'ALIVE', None, 1, 1)
knights = [R, B, G, Y]

class Item:
    def __init__(self, name, attack, defence, value, position, equipped):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.equipped = equipped

A = Item('axe', 2, 0, 40, [2,2], False)
M = Item('magic_staff', 1, 1, 30, [5,2], False)
D = Item('dagger', 1, 0, 20, [2,5], False)
H = Item('helmet', 0, 1, 10, [5,5], False)
items = [A, M, D, H]

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
