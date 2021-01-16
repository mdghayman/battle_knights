from classes import Knight, Item

R = Knight('R', 'red', [0,0], 'ALIVE', None, 1, 1)
B = Knight('B', 'blue', [7,0], 'ALIVE', None, 1, 1)
G = Knight('G', 'green', [7,7], 'ALIVE', None, 1, 1)
Y = Knight('Y', 'yellow', [0,7], 'ALIVE', None, 1, 1)
knights = [R, B, G, Y]

A = Item('A', 'axe', 2, 0, 40, [2,2], False)
M = Item('M', 'magic_staff', 1, 1, 30, [5,2], False)
D = Item('D', 'dagger', 1, 0, 20, [2,5], False)
H = Item('H', 'helmet', 0, 1, 10, [5,5], False)
items = [A, M, D, H]
