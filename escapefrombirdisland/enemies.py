class Enemy
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return hp > 0

class AndeanCockOfTheRock(Enemy):
    def __init__(self):
        self.name = "Andy the Cock-of-the-Rock"
        self.hp = 10
        self.damage = 2

class BlueManakin(Enemy):
    def __init__(self):
        self.name = "Flock of Blue Manakins"
        self.hp = 20
        self.damage = 5

class SatinBowerBird(Enemy):
    def __init__(self):
        self.name = "Satin Bower Bird"
        self.hp = 50
        self.damage = 10
