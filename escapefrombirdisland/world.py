class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
    def intro_text(self):
        return """
        You find yourself in a dimmly lit hallway.
        There are oak wood doors on either side of you. Behind and before you the hallway extends into darkness.
        Gentle cooing can be heard reverberating in the air.
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        Boring Bird Base
        """


class VictoryTile(MapTile):
    def intro_text(self):
        return """
        As you spread your wings you can feel the wind rustling your silky feathers.
        The sun beams down on you as you soar on the updrafts.
        """

world_map =[
    [None,VictoryTile(1,0),None],
    [None,BoringTile(1,1),None],
    [BoringTile(0,2),StartTile(1,2),BoringTile(2,2)],
    [None,BoringTile(1,3),None]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
