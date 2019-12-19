from IntCode import IntCode


def test(x, y):
    comp.reset()
    comp.input_val = [x, y]
    comp.run()
    return comp.output[0]


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])

x = 1010
y = 554
in_beam = False
found = False

while not found:
    x = max(x - 5, 0)
    while not test(x, y) == 1:
        x += 1
    vals = test(x + 99, y), test(x, y - 99), test(x + 99, y - 99)
    if vals == (1, 1, 1):
        print(x, y - 99, x * 10000 + y - 99)
        found = True
    y += 1
