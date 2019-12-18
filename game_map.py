class Tile:
    def __init__(self, block_move=True, door=None, key=None):
        self.block_move = block_move
        self.door = door
        self.key = key

    def blocks(self, keys):
        return self.block_move or (self.door and self.door.lower() not in keys)

    def __repr__(self):
        if self.block_move:
            return "#"
        elif self.door is not None:
            return self.door
        elif self.key is not None:
            return self.key
        else:
            return "."


class GameMap:
    """
    Represents a complete Game Map and all the Tiles on it
    """

    def __init__(self, width, height):
        """
        Create a new map
        :param int width: Size of map in Tiles
        :param int height: Size of map in Tiles
        """
        self.width = width
        self.height = height
        self.tiles = [[Tile() for _ in range(self.width)] for _ in range(self.height)]

    def point_in_map(self, x, y):
        """
        Checks if a given point falls within the current map
        :param x: Target X position
        :param y: Target Y position
        :return: True if desired location is within map bounds
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def is_blocked(self, x, y, keys=None):
        """
        Check if a tile blocks movement
        :param int x: position of Tile on map
        :param int y: position of Tile on map
        :param list keys: keys player has collected
        :return bool: True if tile blocks movement.
        """
        if keys is None: keys = []
        return self.tiles[y][x].blocks(keys)

    def __repr__(self):
        maze = ""
        for y in range(self.height):
            for x in range(self.width):
                maze += str(self.tiles[y][x])
            maze += "\n"

        return maze
