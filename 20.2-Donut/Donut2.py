import collections
from pprint import pprint

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
height = len(grid) - 1
width = len(grid[0]) - 1

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x].isalpha():
            portal = find_dot(x, y)
            if portal:
                dot, (tag_x, tag_y) = portal
                dot_x, dot_y = dot
                edge = dot_x == 2 or dot_x == width - 2 or dot_y == 2 or dot_y == height - 2

                tag = "".join(sorted(grid[y][x] + grid[tag_y][tag_x]))
                if not portals.get(tag):
                    portals[tag] = []
                portals[tag].append(((x, y), dot, edge))

gx, gy, sx, sy = (0, 0, 0, 0)
for link in portals:
    ends = portals[link]
    if len(ends) == 2:
        (a, (a_x, a_y), a_edge), (b, (b_x, b_y), b_edge) = ends
        portal_links[a] = (b_x, b_y, a_edge, link)
        portal_links[b] = (a_x, a_y, b_edge, link)

    elif link == "ZZ":
        goal, (gx, gy), ge = ends[0]
    elif link == "AA":
        start, (sx, sy), se = ends[0]

pprint(portals)
print(portal_links)

bfs = collections.deque([((sx, sy), 0, 0)])
seen = {(sx, sy, 0)}

running = True
while running:
    pos, level, dist = bfs.popleft()

    if pos == (gx, gy) and level == 0:
        print(dist)
        running = False
        break

    for neighbor in neighbors:
        dx, dy = neighbor
        tx, ty = pos
        tx, ty = tx + dx, ty + dy
        t_level = level

        if (tx, ty) in portal_links:
            px, py, p_edge, link = portal_links[(tx, ty)]

            # print(link, (tx, ty), (px, py), p_edge)

            if p_edge and t_level > 0:
                t_level -= 1
                tx, ty = px, py
            elif not p_edge:
                t_level += 1
                tx, ty = px, py

        if (tx, ty, t_level) in seen:
            continue
        seen.add((tx, ty, t_level))

        if grid[ty][tx] == '.':
            p = (tx, ty)
            s = (p, t_level, dist + 1)
            bfs.append(s)


print("complete")
