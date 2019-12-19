from IntCode import IntCode


def point_in_beam(x, y):
    comp.reset()
    comp.input_val = [x, y]
    comp.run()
    return comp.output[0]


def square_in_beam(side_length, starting_x=5, starting_y=5):
    x = starting_x
    y = starting_y
    side = side_length - 1

    while True:
        # reset x to be left of the leftmost edge of the beam
        x = max(x - 5, 0)

        # find the edge of the beam
        while not point_in_beam(x, y) == 1:
            x += 1

        # bottom-left corner of the square is in place, check the other 3 corners
        if point_in_beam(x + side, y) and \
                point_in_beam(x, y - side) and \
                point_in_beam(x + side, y - side):
            return x, y

        # otherwise try the next line
        y += 1


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])
x, y = square_in_beam(100, 1000, 500)
print(x, y - 99, x * 10000 + y - 99)
