class Weapon:
    def _init_(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def _str_(self):
        return self.name

class Egg(Weapon):
    def _init_(self):
        self.name = "Egg"
        self.description = "Just an egg." \
                           "Sure looks yummy. Wonder whose kid it is..."

        self.damage = 5

class Talons(Weapon):
    def _init_(self):
        self.name = "Talons"
        self.description = "Woah there, lassie!" \
                           "Those talons be mighty sharp. Careful not to poke an eye out." \
                           "Your hands are now falcon talons"

        self.damage = 15

def play():
    inventory = ['Egg','Feather','seed(5)']
    print("Escape from Bird Island")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North!")
        elif action_input in ['s', 'S']:
            print("Go South!")
        elif action_input in ['e', 'E']:
            print("Go East!")
        elif action_input in ['w', 'W']:
            print("Go West!")
        else:
            print("Invalid action!")

def get_player_command():
    return input('Action: ')

def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
            pass

    return best_weapon

play()
