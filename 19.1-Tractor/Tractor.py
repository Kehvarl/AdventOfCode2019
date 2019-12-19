from IntCode import IntCode

comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])

width = 50
height = 50

grid = [["." for _ in range(width)] for _ in range(height)]
count = 0
for y in range(height):
    for x in range(width):
        comp.reset()
        comp.input_val = [x, y]
        comp.run()
        if len(comp.output) > 0:
            is_tractor = comp.output.pop()
            grid[y][x] = str(is_tractor)
            if is_tractor == 1:
                count += 1

for line in grid:
    print("".join(line))
print(count)
