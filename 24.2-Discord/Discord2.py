from pprint import pprint


def parse_input(input_string):
    input_grid = {}
    board = [[var for var in line] for line in input_string.split("\n")]

    for in_y in range(5):
        for in_x in range(5):
            input_grid[(0, in_x, in_y)] = board[in_y][in_x]

    return input_grid


def get_adjacent(current_grid, current_level, cell_x, cell_y):
    neighbors = []
    for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        cx, cy = cell_x + dx, cell_y + dy

        if cx < 0:
            # return level -1, x = 1, y = 2
            neighbors.append(current_grid.get((current_level - 1, 1, 2), "."))
        elif cx > 4:
            # return level -1, x = 3, y = 2
            neighbors.append(current_grid.get((current_level - 1, 3, 2), "."))

        elif cy < 0:
            # return level -1, x = 2, y = 1
            neighbors.append(current_grid.get((current_level - 1, 2, 1), "."))

        elif cy > 4:
            # return level -1, x = 2, y = 3
            neighbors.append(current_grid.get((current_level - 1, 2, 1), "."))

        elif cx == 2 and cy == 2:
            if cell_x == 1:
                for _y in range(4):
                    neighbors.append(current_grid.get((current_level + 1, 0, _y), "."))

            elif cell_x == 3:
                for _y in range(4):
                    neighbors.append(current_grid.get((current_level + 1, 4, _y), "."))

            elif cell_y == 1:
                for _x in range(4):
                    neighbors.append(current_grid.get((current_level + 1, _x, 0), "."))

            elif cell_y == 3:
                for _x in range(4):
                    neighbors.append(current_grid.get((current_level + 1, _x, 3), "."))

        else:
            neighbors.append(current_grid.get((current_level, cx, cy), "."))
    return neighbors


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

for iter in range(10):
    for level in range(min_level, max_level + 1):
        for y in range(4):
            for x in range(4):
                count = sum([1 if val == "#" else 0 for val in get_adjacent(grid, level, x, y)])
                if grid.get((level, x, y), ".") == "#" and count != 1:
                    grid[(level, x, y)] = "."
                elif grid.get((level, x, y), ".") == "." and count == 2:
                    grid[(level, x, y)] = "#"
    min_level -= 1
    max_level += 1

print(sum([1 if val == "#" else 0 for val in grid.values()]))

pprint(grid)
