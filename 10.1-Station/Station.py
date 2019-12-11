from math import atan2
import math

test = """.#......##.#..#.......#####...#..
...#.....##......###....#.##.....
..#...#....#....#............###.
.....#......#.##......#.#..###.#.
#.#..........##.#.#...#.##.#.#.#.
..#.##.#...#.......#..##.......##
..#....#.....#..##.#..####.#.....
#.............#..#.........#.#...
........#.##..#..#..#.#.....#.#..
.........#...#..##......###.....#
##.#.###..#..#.#.....#.........#.
.#.###.##..##......#####..#..##..
.........#.......#.#......#......
..#...#...#...#.#....###.#.......
#..#.#....#...#.......#..#.#.##..
#.....##...#.###..#..#......#..##
...........#...#......#..#....#..
#.#.#......#....#..#.....##....##
..###...#.#.##..#...#.....#...#.#
.......#..##.#..#.............##.
..###........##.#................
###.#..#...#......###.#........#.
.......#....#.#.#..#..#....#..#..
.#...#..#...#......#....#.#..#...
#.#.........#.....#....#.#.#.....
.#....#......##.##....#........#.
....#..#..#...#..##.#.#......#.#.
..###.##.#.....#....#.#......#...
#.##...#............#..#.....#..#
.#....##....##...#......#........
...#...##...#.......#....##.#....
.#....#.#...#.#...##....#..##.#.#
.#.#....##.......#.....##.##.#.##
"""

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


def get_angle(point, origin=(0, 0)):
    px, py = point
    ox, oy = origin

    x = px - ox
    y = py - oy

    return atan2(x, y)


def iscolinear(point1, point2, origin=(0, 0)):
    return ((get_angle(point1, origin) -
             get_angle(point2, origin)) == 0)


def to_angle(angle):
    return math.degrees(angle % (2 * math.pi))


def get_distance(point, origin=(0, 0)):
    px, py = point
    ox, oy = origin
    return math.sqrt((px - ox) ** 2 + (py - oy) ** 2)


slope_to = {}
for asteroid in grid:
    slope_to[asteroid] = {}
    for other in grid:
        if other == asteroid:
            continue
        slope_to[asteroid][other] = get_angle(other, asteroid)

# print(slope_to)


visible = 0
base = None
for asteroid in slope_to:
    slopes_used = []
    for slope in slope_to[asteroid]:
        # print(asteroid, slope, slope_to[asteroid][slope])
        if slope_to[asteroid][slope] not in slopes_used:
            slopes_used.append(slope_to[asteroid][slope])

    if len(slopes_used) > visible:
        visible = len(slopes_used)
        base = asteroid
    # print(slopes_used)
    # print(len(slopes_used))

print(base, visible)

angles = {}
for slope in slope_to[base]:
    if slope != base:
        angle = to_angle(get_angle(slope, base))
        angles[angle] = angles.get(angle, [])
        angles[angle].append(slope)

print(angles)

angle = 180.0
deleted = 0


def func(a):
    return (a) % 360


angles_list = sorted(angles.keys())  # , key=func)

print(angles_list)
print(angles[209.74488129694222])

for a in angles_list:
    closest = None
    dist = 0
    for p in angles[a]:
        if closest is None:
            closest = p
            dist = get_distance(p, base)
        else:
            dist_1 = get_distance(p, base)
            if dist_1 < dist:
                closest = p
                dist = dist_1
        if closest is not None:
            deleted += 1
            if p == (17, 7):
                print(deleted, p, dist, a)
            angles[a].remove(p)
