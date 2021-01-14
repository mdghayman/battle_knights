from instances import items, knights



moves = open('moves.txt').read().split('\n')[1:-2]

turns = []
turn = 0

for move in moves:
    turn += 1
    turns[i] = Move(turn, move[0], move[2])

def find_item():
    for item in items:
        if item.position == knight.position:
            item_free = item
    if self.item in items:
        if items.index(self.item) > items.index(self.item):
            pass
        else:
            self.item = item_free
    else:
        self.item = item_free

def attack():
