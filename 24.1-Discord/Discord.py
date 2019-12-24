test1 = """....#
#..#.
#..##
..#..
#...."""

input1 = """##.#.
#..#.
.....
....#
#.###"""

board = [[var for var in line] for line in input1.split("\n")]


def process(grid):
    new_grid = [["" for var in line] for line in grid]

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            count = 0
            for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dx, dy = delta
                cx = x + dx
                cy = y + dy
                if cx < 0 or cx >= len(grid[0]):
                    count += 0
                elif cy < 0 or cy >= len(grid):
                    count += 0
                else:
                    try:
                        if grid[cy][cx] == "#":
                            count += 1
                    except:
                        print(x, dx, cx, y, dy, cy)

            if grid[y][x] == ".":
                if count == 1 or count == 2:
                    new_grid[y][x] = "#"
                else:
                    new_grid[y][x] = "."
            else:
                if count == 1:
                    new_grid[y][x] = "#"
                else:
                    new_grid[y][x] = "."

    return new_grid


boards = []
match = False
while not match:
    board = process(board)
    if board not in boards:
        boards.append(board)
    else:
        match = True
        break

print(board)

flat = sum(board, [])
numbers = ["1" if x == "#" else "0" for x in flat]

print(flat)
print(numbers)
print(int("".join(reversed(numbers)), 2))
