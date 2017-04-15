class MapTile:
    def _init_(self, x, y):
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
        
