

maze = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split("\n")


# Load map
# Get player pos
# Scan to closest door
# scan to key for door
# Can't get key
# scan for next closest door and its key.
# repeat until no doors
# get all keys


def find_bot(data):
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if data[y][x] == "@":
                bot_pos = (x, y)
                return bot_pos


def bfs_search(search_grid, search_maze):
    changed = True
    while changed:
        changed = False
        for y in range(0, len(search_maze)):
            for x in range(0, len(search_maze[0])):
                if not search_maze[y][x] == "#":
                    lowest_neighbor = 1000
                    for neighbor in neighbors:
                        dx, dy = neighbor
                        tx, ty = x + dx, y + dy
                        if 0 <= tx < len(search_maze[0]) and 0 <= ty < len(search_maze):
                            lowest_neighbor = min(lowest_neighbor, search_grid[ty][tx])

                    if search_grid[y][x] > lowest_neighbor + 1:
                        search_grid[y][x] = lowest_neighbor + 1
                        changed = True
    return search_grid


pos = find_bot(maze)
bot_x, bot_y = pos

neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]

points_of_interest = {}
bfs_poi = {}
graph_interest = {}

for y in range(0, len(maze)):
    for x in range(0, len(maze[0])):
        tile = maze[y][x]
        if tile == "@" or (tile.isalpha() and tile.islower()):
            graph_interest[tile] = []
            bfs_poi[tile] = ([[1000 for _ in range(len(maze[0]))] for _ in range(len(maze))])
            bfs_poi[tile][y][x] = 0
            points_of_interest[tile] = (x, y)

for poi in bfs_poi:
    bfs_poi[poi] = bfs_search(bfs_poi[poi], maze)

    print(poi, points_of_interest[poi])
    for line in bfs_poi[poi]:
        print(" ".join([str(x).zfill(2) if (x != 1000) else "##" for x in line]))
    print()
