example1 = open("input.txt", "r").read()

# grid = [[val for val in line] for line in example1.split("\n")]
grid = example1.split("\n")
length = 0

for line in grid:
    length = max(len(line), length)

out = []
for line in grid:
    out.append(line[::-1].zfill(length)[::-1])

grid = out
scanned = []

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_dot(dot_x, dot_y):
    for (_dx, _dy) in neighbors:
        if 0 <= dot_x + _dx < len(grid[0]) and 0 <= dot_y + _dy < len(grid):
            if grid[dot_y + _dy][dot_x + _dx] == ".":
                return (dot_x + _dx, dot_y + _dy), (dot_x - _dx, dot_y - _dy)  # (dot), (tag)
    return False


# Find portals
# For each portal:
# Inner edge:  recurse
# Outer edge: return

portals = {}
portal_links = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x].isalpha():
            portal = find_dot(x, y)
            if portal:
                dot, (tag_x, tag_y) = portal
                tag = "".join(sorted(grid[y][x] + grid[tag_y][tag_x]))
                if not portals.get(tag):
                    portals[tag] = []
                portals[tag].append(((x, y), dot))

gx, gy, sx, sy = (0, 0, 0, 0)
for link in portals:
    ends = portals[link]
    if len(ends) == 2:
        (a, a_dot), (b, b_dot) = ends
        portal_links[a] = b_dot
        portal_links[b] = a_dot
    elif link == "ZZ":
        goal, (gx, gy) = ends[0]
    elif link == "AA":
        start, (sx, sy) = ends[0]

print(portals)
print(portal_links)

bfs = [[1000 for _ in range(len(grid[0]))] for _ in range(len(grid))]
bfs[gy][gx] = 0
"""
Use Dijkstra's Algorithm to calculate the movement score towards
goals in this map
"""
changed = True
while changed:
    changed = False
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            if grid[y][x] == ".":
                lowest_neighbor = 1000
                for neighbor in neighbors:
                    dx, dy = neighbor
                    tx, ty = x + dx, y + dy
                    if (tx, ty) in portal_links:
                        tx, ty = portal_links[(tx, ty)]
                    if 0 <= tx < len(grid[0]) and 0 <= ty < len(grid):
                        lowest_neighbor = min(lowest_neighbor, bfs[ty][tx])

                if bfs[y][x] > lowest_neighbor + 1:
                    bfs[y][x] = lowest_neighbor + 1
                    changed = True

printable_bfs = [[str(i).zfill(3) if i < 1000 else "###" for i in line] for line in bfs]
print("\n".join([" ".join(line) for line in printable_bfs]))
print()
print(bfs[sy][sx])
