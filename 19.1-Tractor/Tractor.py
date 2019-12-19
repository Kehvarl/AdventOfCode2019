from IntCode import IntCode

comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])

width = 100
height = 100

grid = [["." for _ in range(width)] for _ in range(height)]
slopes = []
count = 0
for y in range(height):
    start = None
    end = None
    for x in range(width):
        comp.reset()
        comp.input_val = [x, y]
        comp.run()
        if len(comp.output) > 0:
            is_tractor = comp.output.pop()
            grid[y][x] = str(is_tractor)
            if is_tractor == 1:
                count += 1
                if start is None:
                    start = x
            if is_tractor == 0 and end is None and start is not None:
                end = x
        if y > 0 and start is not None and end is not None:
            slopes.append((y, (start / y), (end / y)))

for line in grid:
    print("".join(line))
print(count)

print(slopes)
