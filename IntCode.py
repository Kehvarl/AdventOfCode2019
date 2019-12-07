class IntCode:
    def __init__(self, initial_state=None, verb=None, noun=None):
        self.initial_state = initial_state[:]
        self.state = []
        self.verb = verb
        self.noun = noun

        self.program_counter = 0

        self.running = False
        self.error = False
        self.error_detail = None

        self.output = ""

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
        self.output = ""

    def decode_op(self, opcode):
        opcode = str(opcode).zfill(5)
        if len(opcode) < 5:
            c = 0
        else:
            c = opcode[0]
        if len(opcode) < 4:
            b = 0
        else:
            b = opcode[1]
        if len(opcode) < 3:
            a = 0
        else:
            a = opcode[2]
        op = opcode[-2:]
        return (int(a), int(b), int(c), int(op))

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
        (ma, mb, mc, op) = self.decode_op(self.load(1, self.program_counter))
        if op == 1:  # add
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(1, self.program_counter + 3)  #
            self.store(c, a + b)  # Add
            self.program_counter += 4
        elif op == 2:  # mul
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(1, self.program_counter + 3)
            self.store(c, a * b)  # Multiply
            self.program_counter += 4
        elif op == 3:  # Interactive Input
            ma = 1
            a = self.load(ma, self.program_counter + 1)
            val = input("input>")
            self.store(a, int(val))
            self.program_counter += 2
        elif op == 4:  # Output
            a = self.load(ma, self.program_counter + 1)
            self.output += str(a)
            self.program_counter += 2
        elif op == 5:  # jmp if True
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            if a != 0:
                self.program_counter = b
            self.program_counter += 3
        elif op == 6:  # jmp if False
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            if a == 0:
                self.program_counter = b
            self.program_counter += 3
        elif op == 7:  # less-than
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(1, self.program_counter + 3)
            if a < b:
                self.store(c, 1)
            else:
                self.store(c, 0)
            self.program_counter += 4
        elif op == 8:  # equals
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load(1, self.program_counter + 3)
            if a == b:
                self.store(c, 1)
            else:
                self.store(c, 0)
            self.program_counter += 4
        elif op == 99:
            self.running = False
        else:
            self.running = False
            self.error = True
            self.error_detail = "Invalid OpCode Encountered: {} at {}.".format(op, self.program_counter)


if __name__ == "__main__":
    # prog = [1,0,0,3,99] # state[3] == 2
    # prog = [1,9,10,3,2,3,11,0,99,30,40,50] # state[1] == 3500
    # prog = [3,0,4,0,99] # state[0] = Input
    # prog = [1002, 4, 3, 4, 33] # state[4] = 99
    # prog = [1101,100,-1,4,0] # state[4] = 99
    # prog = [3,9,8,9,10,9,4,9,99,-1,8] # input == 8?
    # prog = [3,9,7,9,10,9,4,9,99,-1,8] # input < 8?
    # prog = [3,3,1108,-1,8,3,4,3,99] # immediate input == 8?
    prog = [3, 3, 1107, -1, 8, 3, 4, 3, 99]  # immediate input < 8?
    # 999   < 8, 1000 = 8, 1001 > 8
    # prog = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    comp = IntCode(prog)
    comp.run()
    print(comp.state)
    print(comp.output)
