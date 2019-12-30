

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


pos = find_bot(maze)
bot_x, bot_y = pos

bfs = [[1000 for _ in range(len(maze[0]))] for _ in range(len(maze))]

bfs[bot_y][bot_x] = 0

neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]
"""
Use Dijkstra's Algorithm to calculate the movement score towards
goals in this map
"""
changed = True
while changed:
    changed = False
    for y in range(0, len(maze)):
        for x in range(0, len(maze[0])):
            if not maze[y][x] == "#":
                lowest_neighbor = 1000
                for neighbor in neighbors:
                    dx, dy = neighbor
                    tx, ty = x + dx, y + dy
                    if 0 <= tx < len(maze[0]) and 0 <= ty < len(maze):
                        lowest_neighbor = min(lowest_neighbor, bfs[ty][tx])

                if bfs[y][x] > lowest_neighbor + 1:
                    bfs[y][x] = lowest_neighbor + 1
                    changed = True

for line in bfs:
    print(" ".join([str(x).zfill(2) if (x != 1000) else "##" for x in line]))
