from game_map import GameMap, Tile
from dijkstra_map import DijkstraMap

maze = """#########
#b.A.@.a#
#########""".split("\n")

riddle = GameMap(len(maze[0]), len(maze))
px, py = (0, 0)

for y in range(len(maze)):
    for x in range(len(maze[0])):
        if maze[y][x] != "#":
            riddle.tiles[y][x].block_move = False
        if maze[y][x] == "@":
            px = x
            py = y

        if maze[y][x].isalpha() and maze[y][x].isupper():
            riddle.tiles[y][x].door = maze[y][x]
        if maze[y][x].isalpha() and not maze[y][x].isupper():
            riddle.tiles[y][x].key = maze[y][x]

print(riddle)

solver = DijkstraMap(riddle, [(px, py, 0)])
solver.recalculate_map()
print(solver)

# Load map
# Get player pos
# Scan to closest door
# scan to key for door
# Can't get key
# scan for next closest door and its key.
# repeat until no doors
# get all keys
