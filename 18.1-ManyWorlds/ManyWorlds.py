from game_map import GameMap, Tile
from dijkstra_map import DijkstraMap

maze = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split("\n")

riddle = GameMap(len(maze[0]), len(maze))
px, py = (0, 0)
map_keys = []
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
            map_keys.append((x, y, 0))

print(riddle)

solver = DijkstraMap(riddle, map_keys)
solver.recalculate_map()
print(solver)
print(solver.get_move_options(px, py))

# Load map
# Get player pos
# Scan to closest door
# scan to key for door
# Can't get key
# scan for next closest door and its key.
# repeat until no doors
# get all keys
