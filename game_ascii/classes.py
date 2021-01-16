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
    def __init__(self, name, attack, defence, value, position, equipped):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.value = value
        self.position = position
        self.equipped = equipped


