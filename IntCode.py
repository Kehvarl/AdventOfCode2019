class IntCode:
    def __init__(self, initial_state=None, verb=None, noun=None):
        self.initial_state = initial_state
        self.state = []
        self.verb = verb
        self.noun = noun

        self.program_counter = 0

        self.running = False
        self.error = False
        self.error_detail = None

        self.reset()

    def reset(self):
        self.state = self.initial_state
        if self.verb is not None:
            self.state[1] = self.verb
        if self.noun is not None:
            self.state[2] = self.noun

        self.program_counter = 0

        self.running = True
        self.error = False
        self.error_detail = None

    def decode_op(self, opcode):
        opcode = str(opccode)
        if len(opcode) < 5:
            a = 0
        else:
            a = opcode[0]
        if len(opcode) < 4:
            b = 0
        else:
            b = opcode[1]
        if len(opcode) < 3:
            b = 0
        else:
            b = opcode[2]
        op = opcode[-2:]
        return (a, b, c, op)

    def load(self, mode, pointer):
        if mode == 1:
            return self.state[pointer]
        else:
            return self.state[self.state[pointer]]

    def store(self, pointer, value):
        self.state[pointer] = value

    def run(self):
        while self.running:
            self.step()

    def step(self):
        (ma, mb, mc, op) = self.decode_op(self.load(self.program_counter))
        if op == 1:  # add indirect
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(mc, self.program_counter + 3)
            self.store(c, a + b)  # Add
            self.program_counter += 4
        elif op == 2:  # mul indirect
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(mc, self.program_counter + 3)
            self.store(c, a * b)  # Multiply
            self.program_counter += 4
        elif op == 3:
            a = self.load(ma, self.program_counter + 1)
            val = input()
            self.store(a, 1)
            self.program_counter += 2
        elif op == 4:
            a = self.load(ma, self.program_counter + 1)
            print(a)
            self.program_counter += 2
        elif op == 99:
            self.running = False
        else:
            self.running = False
            self.error = True
            self.error_detail = "Invalid OpCode Encountered: {} at {}.".format(op, self.program_counter)
