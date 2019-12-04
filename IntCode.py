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
