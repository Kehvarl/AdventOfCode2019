test = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

grid = {}

y = 0
for line in test.split("\n"):
    x = 0
    for char in line:
        if char == "#":
            grid[(x, y)] = (x, y)
        x += 1
    y += 1

# print(grid)

slope_to = {}
for asteroid in grid:
    x1, y1 = asteroid
    slope_to[asteroid] = {}
    for other in grid:
        if other == asteroid:
            continue
        x2, y2 = other
        if y2 == y1:
            slope = 1000
        else:
            slope = (x2 - x1) / (y2 - y1)
        slope_to[asteroid][other] = slope

# print(slope_to)


visible = []
for asteroid in slope_to:
    slopes_used = []
    for slope in slope_to[asteroid]:
        # print(asteroid, slope, slope_to[asteroid][slope])
        if slope_to[asteroid][slope] not in slopes_used:
            slopes_used.append(slope_to[asteroid][slope])
        elif asteroid == (11, 13):
            print(asteroid, slope, slope_to[asteroid][slope])

    visible.append(len(slopes_used))
    # print(slopes_used)
    # print(len(slopes_used))

print(max(visible))
