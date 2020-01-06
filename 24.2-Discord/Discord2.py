from pprint import pprint


def parse_input(input_string):
    input_grid = {}
    board = [[var for var in line] for line in input_string.split("\n")]

    for in_y in range(5):
        for in_x in range(5):
            input_grid[(0, in_x, in_y)] = board[in_y][in_x]

    return input_grid


def get_adjacent(current_grid, current_level, cell_x, cell_y):
    low = level
    high = level
    neighbors = []
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cx, cy = cell_x + dx, cell_y + dy

        if cx < 0:
            # return level -1, x = 1, y = 2
            neighbors.append(current_grid.get((current_level - 1, 1, 2), "."))
            low -= 1
        elif cx > 4:
            # return level -1, x = 3, y = 2
            neighbors.append(current_grid.get((current_level - 1, 3, 2), "."))
            low -= 1
        elif cy < 0:
            # return level -1, x = 2, y = 1
            neighbors.append(current_grid.get((current_level - 1, 2, 1), "."))
            low -= 1
        elif cy > 4:
            # return level -1, x = 2, y = 3
            neighbors.append(current_grid.get((current_level - 1, 2, 1), "."))
            low -= 1
        elif cx == 2 and cy == 2:
            if cell_x == 1:
                for _y in range(5):
                    neighbors.append(current_grid.get((current_level + 1, 0, _y), "."))
                    high += 1
            elif cell_x == 3:
                for _y in range(5):
                    neighbors.append(current_grid.get((current_level + 1, 4, _y), "."))
                    high += 1
            elif cell_y == 1:
                for _x in range(5):
                    neighbors.append(current_grid.get((current_level + 1, _x, 0), "."))
                    high += 1
            elif cell_y == 3:
                for _x in range(5):
                    neighbors.append(current_grid.get((current_level + 1, _x, 3), "."))
                    high += 1
        else:
            neighbors.append(current_grid.get((current_level, cx, cy), "."))
    return neighbors, low, high


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

grid = parse_input(test)
min_level = 0
max_level = 0

print(sum([1 if val == "#" else 0 for val in grid.values()]))

for _ in range(2):
    for level in range(min_level, max_level + 1):
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 2:
                    continue

                adjacent, low, high = get_adjacent(grid, level, x, y)
                min_level = min(min_level, low)
                max_level = max(max_level, high)

                count = sum([1 if val == "#" else 0 for val in adjacent])

                if grid.get((level, x, y), ".") == "#" and count != 1:
                    grid[(level, x, y)] = "."
                elif grid.get((level, x, y), ".") == "." and count in [1, 2]:
                    grid[(level, x, y)] = "#"


print(sum([1 if val == "#" else 0 for val in grid.values()]))

for level in range(min_level, max_level + 1):
    print(level)
    for y in range(5):
        line = ""
        for x in range(5):
            line += grid.get((level, x, y), ".")
        print(line)
