def int_code(prog, noun=None, verb=None):
    pc = 0
    if noun is not None:
        prog[1] = noun

    if verb is not None:
        prog[2] = verb

    running = True
    while running:
        op = prog[pc]
        if op == 1:  # add indirect
            a = prog[prog[pc + 1]]
            b = prog[prog[pc + 2]]
            c = prog[pc + 3]
            prog[c] = a + b
            pc += 4
        elif op == 2:  # mul indirect
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


class IntCode:
    def __init__(self, initial_state=None, verb=None, noun=None):
        self.initial_state = initial_state
        self.state = []
        self.verb = verb
        self.noun = noun

        self.program_counter = 0
        self.memory_register = 0

        self.running = False

        self.reset()

    def reset(self):
        self.state = self.initial_state
        if self.verb is not None:
            self.state[1] = self.verb
        if self.noun is not None:
            self.state[2] = self.noun

        self.program_counter = 0
        self.memory_register = 0
        self.running = True

    def load_indirect(self, pointer):
        return self.state[self.state[pointer]]

    def load(self, pointer):
        return self.state[pointer]

    def store(self, pointer, value):
        self.state[pointer] = value

    def run(self):
        while self.running:
            self.step()

    def step(self):
        op = self.state[self.program_counter]
        if op == 1:  # add indirect
            a = self.load_indirect(self.program_counter + 1)
            b = self.load_indirect(self.program_counter + 2)
            c = self.load(self.program_counter + 3)
            self.store(c, a + b)  # Add
            self.program_counter += 4
        elif op == 2:  # mul indirect
            a = self.load_indirect(self.program_counter + 1)
            b = self.load_indirect(self.program_counter + 2)
            c = self.load(self.program_counter + 3)
            self.store(c, a * b)  # Multiply
            self.program_counter += 4
        elif op == 99:
            self.running = False
        else:
            self.running = False
