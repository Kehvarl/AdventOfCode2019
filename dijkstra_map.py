class DijkstraMap:
    """
    Python implementation of Dijkstra Maps
    Source: http://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps
            http://www.roguebasin.com/index.php?title=Dijkstra
    """

    # X, Y Transitions to the 4 neighboring cells
    neighbors = [(0, -1),
                 (-1, 0), (1, 0),
                 (0, 1)]

    def __init__(self, game_map, goals=None):
        """
        Create a Map  showing the movement score of various tiles
        :param Map.game_map.GameMap game_map: Current level map
        """
        if goals is None:
            self.goals = []
        else:
            self.goals = goals
        self.game_map = game_map
        self.tiles = self._clear_map()

    def add_goal(self, x, y, score=0):
        """
        Add a goal tile to the map
        :param int x: Tile X coordinate
        :param int y: Tile Y coordinate
        :param int score: Desirability of this location (default: 0)
        """
        self.goals.append((x, y, score))

    def recalculate_map(self):
        """
        Use Dijkstra's Algorithm to calculate the movement score towards
        goals in this map
        """
        changed = True
        while changed:
            changed = False
            for y in range(0, self.game_map.height):
                for x in range(0, self.game_map.width):
                    if not self.game_map.is_blocked(x, y):
                        lowest_neighbor = self._get_lowest_neighbor_value(x, y)
                        if self.tiles[y][x] > lowest_neighbor + 1:
                            self.tiles[y][x] = lowest_neighbor + 1
                            changed = True

    def get_move_options(self, x, y):
        """
        Return a list of ideal moves from a given point
        :param x: Entity X Coordinate
        :param y: Entity Y Coordinate
        :return list: Recommended moves
        """
        best = self._get_lowest_neighbor_value(x, y)
        moves = []
        for dx, dy in DijkstraMap.neighbors:
            tx, ty = x + dx, y + dy
            if self.game_map.point_in_map(tx, ty) and self.tiles[ty][tx] == best:
                moves.append({'move': (dx, dy)})
        return moves

    def _clear_map(self, default=100):
        """
        Reset the map scores to an arbitrary value and populate goals
        :param int default: the initial value to set for each cell
        """
        tiles = [
            [default
             for _ in range(self.game_map.width)]
            for _ in range(self.game_map.height)]

        for x, y, score in self.goals:
            tiles[y][x] = score

        return tiles

    def _get_lowest_neighbor_value(self, x, y):
        """
        Get the score in the current lowest-valued neighbor cell
        :param x: Current X Coordinate
        :param y: Current Y Coordinate
        :return int: Lowest neighboring value
        """
        lowest = 100
        for dx, dy in DijkstraMap.neighbors:
            tx, ty = x + dx, y + dy
            if self.game_map.point_in_map(tx, ty):
                lowest = min(lowest, self.tiles[ty][tx])
        return lowest

    def __repr__(self):
        maze = ""
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                maze += "{0: ^3}".format(str(self.tiles[y][x]))
            maze += "\n"

        return maze
