example1 = open("example1.txt", "r").read()

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
height = len(grid) - 1
width = len(grid[0]) - 1
edges = [0, 1, height, height - 1, width, width - 1]
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x].isalpha():
            portal = find_dot(x, y)
            if portal:
                edge = x in edges or y in edges
                dot, (tag_x, tag_y) = portal
                tag = "".join(sorted(grid[y][x] + grid[tag_y][tag_x]))
                if not portals.get(tag):
                    portals[tag] = []
                portals[tag].append(((x, y), dot, edge))

gx, gy, sx, sy = (0, 0, 0, 0)
for link in portals:
    ends = portals[link]
    if len(ends) == 2:
        (a, (a_x, a_y), a_edge), (b, (b_x, b_y), b_edge) = ends
        portal_links[a] = (b_x, b_y, b_edge)
        portal_links[b] = (a_x, a_y, a_edge)

    elif link == "ZZ":
        goal, (gx, gy), ge = ends[0]
    elif link == "AA":
        start, (sx, sy), se = ends[0]

print(portals)
print(portal_links)

x, y = sx, sy
level = 0
path = [(0, sx, sy)]
searched = {(0, sx, sy): 0}

running = True
while running:
    for neighbor in neighbors:
        dx, dy = neighbor
        x, y = x + dx, y + dy
        if (x, y) in portal_links:
            px, py, pe = portal_links[(x, y)]

            if pe and level > 0:
                level -= 1
                x, y = px, py
            elif not pe:
                level += 1
                x, y = px, py

        if (level, x, y) not in searched:
            break
    else:
        level, x, y = path[-1]
        path = path[:-1]

    if len(path) == 0:
        running = False
        break

    searched[(level, x, y)] = 0

print("complete")
print(path)
print(searched)
