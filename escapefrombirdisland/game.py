from player import Player
import world

def play():
    inventory = ['Egg','Feather','seed(5)']
    print("Escape from Bird Island")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            player.move_north
        elif action_input in ['s', 'S']:
            player.move_south
        elif action_input in ['e', 'E']:
            player.move_east
        elif action_input in ['w', 'W']:
            player.move_west
        elif action_input in ['i', 'I']:
            player.print_inventory()
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
