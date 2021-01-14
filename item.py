class Item:
    def __init__(self, attack, defence, value, position, equipped):
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.equipped = equipped


class Move:
    def __init__(self, turn, knight, direction):
        self.turn = turn
        self.knight = knight
        self.direction = direction
