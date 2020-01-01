example1 = open("example1.txt", "r").read()

# grid = [[val for val in line] for line in example1.split("\n")]
grid = example1.split("\n")
length = 0

for line in grid:
    length = max(len(line), length)

out = []
for line in grid:
    out.append(line[::-1].zfill(length)[::-1])
print(out)

grid = out
scanned = []

neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def find_dot(x, y):
    for (dx, dy) in neighbors:
        if 0 <= x + dx < len(grid[0]) and 0 <= y + dy < len(grid):
            if grid[y + dy][x + dx] == ".":
                return (x + dx, y + dy), (x - dx, y - dy)  # (dot), (tag)
    return False


portals = {}
portal_links = {}
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x].isalpha():
            portal = find_dot(x, y)
            if portal:
                dot, (tagx, tagy) = portal
                tag = "".join(sorted(grid[y][x] + grid[tagy][tagx]))
                if not portals.get(tag):
                    portals[tag] = []
                portals[tag].append(dot)

print(portals)
