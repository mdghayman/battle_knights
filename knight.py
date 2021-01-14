class Knight:

    def __init__(self, position, status, item, attack, defence):
        self.position = position
        self.status = status
        self.item = item
        self.attack = attack
        self.defence = defence

    def move(direction):
        if self.status == 'ALIVE':
            if direction = 'N':
                self.position[0] -= 1
            if direction = 'S':
                self.position[0] += 1
            if direction = 'W':
                self.position[1] -= 1
            if direction = 'E':
                self.position[1] += 1
        if self.position[0] not in range(8):
            drown()
        if self.position[1] not in range(8):
            drown()

    def pickup(item):
        self.item = item

    def attack():
        pass

    def drown():
        self.position = Null
        self.status = 'DROWNED'
        drop(self.item)
