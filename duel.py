class Goblin:


    def __init__(self):
        self.attack = 5
        self.defense = 7
        self.hitpoints = 10

    def report(self):
        if self.hitpoints > 0:
            return "i am fine"
        else:
            return "i am in bad shape"

    def attack(self):
        print(self.attack)
