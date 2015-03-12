class Goblin:

    @classmethod
    def stats(self):
        print(self.attack)
        print(self.defense)
        print(self.hitpoints)

    def __init__(self):
        self.attack = 5
        self.defense = 7
        self.hitpoints = 10

    def report(self):
        if self.hitpoints > 0:
            return "i am fine"
        else:
            return "i am in bad shape"
