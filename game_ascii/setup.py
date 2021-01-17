class Knight:
    def __init__(self, code, name, position, status, item, attack, defence):
        self.code = code
        self.name = name
        self.position = position
        self.status = status
        self.item = item
        self.attack = attack
        self.defence = defence

class Item:
    def __init__(self, code, name, attack, defence, value, position, holder):
        self.code = code
        self.name = name
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.holder = holder

R = Knight('R', 'red', [0,0], 'ALIVE', None, 1, 1)
B = Knight('B', 'blue', [7,0], 'ALIVE', None, 1, 1)
G = Knight('G', 'green', [7,7], 'ALIVE', None, 1, 1)
Y = Knight('Y', 'yellow', [0,7], 'ALIVE', None, 1, 1)
knights = [R, B, G, Y]

A = Item('A', 'axe', 2, 0, 40, [2,2], None)
M = Item('M', 'magic_staff', 1, 1, 30, [5,2], None)
D = Item('D', 'dagger', 1, 0, 20, [2,5], None)
H = Item('H', 'helmet', 0, 1, 10, [5,5], None)
items = [A, M, D, H]
