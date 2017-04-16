class Enemy
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return hp > 0
class PygmyBushtit(Enemy):
    def __init__(self):
        self.name = "Pygmy Bushtits: Islander bois, but Birds."
        self.hp = 5
        self.damage = 1

class AndeanCockOfTheRock(Enemy):
    def __init__(self):
        self.name = "Andy the Cock-of-the-Rock: The Compensator."
        self.hp = 10
        self.damage = 2

class BlueManakin(Enemy):
    def __init__(self):
        self.name = "Flock of Blue Manakins: Cutest fembirds you eer did meet."
        self.hp = 20
        self.damage = 5
class YellowBelliedSapSucker(Enemy):
    def __init__(self):
        self.name = "Yellow Bellied Sap Sucker: The Lumbersexual."
        self.hp = 40
        self.damage = 10

class SatinBowerBird(Enemy):
    def __init__(self):
        self.name = "Satin Bower Bird: Mr. Grey didn't stand a chance."
        self.hp =80
        self.damage = 15
