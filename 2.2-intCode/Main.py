def int_code(prog, noun=None, verb=None):
    pc = 0
    if noun is not None:
        prog[1] = noun

    if verb is not None:
        prog[2] = verb

    running = True
    while running:
        op = prog[pc]
        if op == 1:
            a = prog[prog[pc + 1]]
            b = prog[prog[pc + 2]]
            c = prog[pc + 3]
            prog[c] = a + b
            pc += 4
        elif op == 2:
            a = prog[prog[pc + 1]]
            b = prog[prog[pc + 2]]
            c = prog[pc + 3]
            prog[c] = a * b
            pc += 4
        elif op == 99:
            running = False
        else:
            running = False
            print("Invalid op code {} at {} !!!".format(op, pc))
    return prog


def main():
    # print (int_code ([1,9,10,3,2,3,11,0,99,30,40,50]))
    # print (int_code([1,0,0,0,99]))
    prog = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 6, 19, 23, 1, 23, 13, 27, 2, 6, 27, 31, 1,
            5,
            31, 35, 2, 10, 35, 39, 1, 6, 39, 43, 1, 13, 43, 47, 2, 47, 6, 51, 1, 51, 5, 55, 1, 55, 6, 59, 2, 59, 10, 63,
            1,
            63, 6, 67, 2, 67, 10, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 2, 10, 83, 87, 1, 87, 6, 91, 2, 9, 91,
            95,
            1, 95, 5, 99, 1, 5, 99, 103, 1, 103, 10, 107, 1, 9, 107, 111, 1, 6, 111, 115, 1, 115, 5, 119, 1, 10, 119,
            123,
            2, 6, 123, 127, 2, 127, 6, 131, 1, 131, 2, 135, 1, 10, 135, 0, 99, 2, 0, 14, 0
            ]

    magic_number = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            test = int_code(prog[:], noun, verb)
            if test[0] == magic_number:
                print(noun, verb, test[0])  # 98 20 19690720


main()
