class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.name


class Egg(Weapon):
    def __init__(self):
        self.name = "Egg"
        self.description = "Just an egg." \
                           "Sure looks yummy. Wonder whose kid it is..."
        self.damage = 5


class Talons(Weapon):
    def __init__(self):
        self.name = "Talons"
        self.description = "Woah there, lassie!" \
                           "Those talons be mighty sharp. Careful not to poke an eye out." \
                           "Your hands are now falcon talons"

        self.damage = 15
