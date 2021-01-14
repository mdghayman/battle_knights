class Item:
    def __init__(self, position, attack, defence):
        self.attack = attack
        self.defence = defence

Axe = Item([2,2], 2, 0)
MagicStaff = Item([5,2], 1, 1)
Dagger = Item([2,5], 1, 0)
Helmet = Item([5,5], 0, 1)



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
                if self.position[0] > 0:
                    self.position[0] = self.position[0] - 1
                else:
                    drown()
            if direction = 'S':
                if self.position[0] < 7:
                    self.position[0] = self.position[0] + 1
                else:
                    drown()
            if direction = 'W':
                if self.position[1] > 0:
                    self.position[1] = self.position[1] - 1
                else:
                    drown()
            if direction = 'E':
                if self.position[1] < 7:
                    self.position[1] = self.position[1] + 1
                else:
                    drown()

    def pickup():
        pass

    def drop():
        pass

    def attack():
        pass

    def drown():
        self.position = Null
        self.status = 'DROWNED'
        drop(self.item)



R = Knight([0,0], 'ALIVE', Null, 1, 1)
B = Knight([7,0], 'ALIVE', Null, 1, 1)
G = Knight([7,7], 'ALIVE', Null, 1, 1)
Y = Knight([0,7], 'ALIVE', Null, 1, 1)
