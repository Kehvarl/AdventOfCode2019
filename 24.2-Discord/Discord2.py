from pprint import pprint


def parse_input(input_string):
    input_grid = set()
    board = [[var for var in line] for line in input_string.split("\n")]

    for in_y in range(5):
        for in_x in range(5):
            if board[in_y][in_x] == "#":
                input_grid.add((0, in_x, in_y))

    return input_grid


def get_adjacent(current_grid, current_level, cell_x, cell_y):
    low = current_level
    high = current_level
    neighbors = []
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cx, cy = cell_x + dx, cell_y + dy

        if cx < 0:
            # return level -1, x = 1, y = 2
            neighbors.append((current_level - 1, 1, 2))
            low -= 1
        elif cx > 4:
            # return level -1, x = 3, y = 2
            neighbors.append((current_level - 1, 3, 2))
            low -= 1
        elif cy < 0:
            # return level -1, x = 2, y = 1
            neighbors.append((current_level - 1, 2, 1))
            low -= 1
        elif cy > 4:
            # return level -1, x = 2, y = 3
            neighbors.append((current_level - 1, 2, 3))
            low -= 1
        elif cx == 2 and cy == 2:
            if cell_x == 1:
                for _y in range(5):
                    neighbors.append((current_level + 1, 0, _y))
                    high += 1
            elif cell_x == 3:
                for _y in range(5):
                    neighbors.append((current_level + 1, 4, _y))
                    high += 1
            elif cell_y == 1:
                for _x in range(5):
                    neighbors.append((current_level + 1, _x, 0))
                    high += 1
            elif cell_y == 3:
                for _x in range(5):
                    neighbors.append((current_level + 1, _x, 4))
                    high += 1
        else:
            neighbors.append((current_level, cx, cy))

    return neighbors, low, high


def step_minute(grid):
    min_level = min(l for l, x, y in grid)
    max_level = max(l for l, x, y in grid)
    new_grid = set()

    for level in range(min_level - 1, max_level + 2):
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 2:
                    continue

                adjacent, low, high = get_adjacent(grid, level, x, y)
                min_level = min(min_level, low)
                max_level = max(max_level, high)

                count = sum(1 for val in adjacent if val in grid)

                if (level, x, y) in grid and count == 1:
                    new_grid.add((level, x, y))
                elif (level, x, y) not in grid and count in [1, 2]:
                    new_grid.add((level, x, y))
    return new_grid


input1 = """##.#.
#..#.
.....
....#
#.###"""

test = """....#
#..#.
#.?##
..#..
#...."""

grid = parse_input(input1)

# print(sum([1 if val == "#" else 0 for val in grid.values()]))

# adjacent, low, high = get_adjacent(grid, 1, 4, 4)

# count = sum([1 if val == "#" else 0 for val in adjacent])

# print(count)
# print(adjacent)
for i in range(200):
    grid = step_minute(grid)

print(len(grid))

min_level = min(l for l, x, y in grid)
max_level = max(l for l, x, y in grid)
for level in range(min_level, max_level + 1):
    print(level)
    for y in range(5):
        line = ""
        for x in range(5):
            line += ("#" if (level, x, y) in grid else ".")
        print(line)
print()
