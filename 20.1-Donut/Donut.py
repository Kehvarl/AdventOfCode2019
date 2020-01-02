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
    for (dx, dy) in neighbors:
        if 0 <= dot_x + dx < len(grid[0]) and 0 <= dot_y + dy < len(grid):
            if grid[dot_y + dy][dot_x + dx] == ".":
                return (dot_x + dx, dot_y + dy), (dot_x - dx, dot_y - dy)  # (dot), (tag)
    return False


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

for link in portals:
    ends = portals[link]
    if len(ends) == 2:
        (a, a_dot), (b, b_dot) = ends
        portal_links[a] = b_dot
        portal_links[b] = a_dot

print(portal_links)
