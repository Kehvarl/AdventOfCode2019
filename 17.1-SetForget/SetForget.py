from IntCode import IntCode

comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])
comp.run()

display = [chr(c) for c in comp.output]

test_data = """..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..""".split("\n")


test_data = ("".join(display)).strip().split("\n")

print(test_data)
print(("".join(display)).strip())

grid = [[test_data[y][x] for x in range(len(test_data[0]))] for y in range(len(test_data))]

print(grid)
intersections = []

for y in range(1, len(test_data) - 1):
    for x in range(1, len(test_data[0]) - 1):
        if test_data[y][x] != ".":
            if test_data[y - 1][x] != "." and \
                    test_data[y + 1][x] != "." and \
                    test_data[y][x - 1] != "." and \
                    test_data[y][x + 1] != ".":
                intersections.append(x * y)

print(intersections)
print(sum(intersections))

