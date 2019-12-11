class IntCode:
    def __init__(self, initial_state=None, verb=None, noun=None, input_val=None):
        self.initial_state = initial_state
        self.state = []
        self.verb = verb
        self.noun = noun
        self.input_val = input_val

        self.program_counter = 0
        self.relative_base = 0

        self.running = False
        self.completed = False
        self.error = False
        self.error_detail = None

        self.output = []

        self.reset()

    def reset(self):
        self.state = self.initial_state[:]
        if self.verb is not None:
            self.state[1] = self.verb
        if self.noun is not None:
            self.state[2] = self.noun

        self.program_counter = 0
        self.relative_base = 0

        self.running = True
        self.completed = False
        self.error = False
        self.error_detail = None
        self.output = []

    # noinspection PyMethodMayBeStatic
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
        return int(a), int(b), int(c), int(op)

    def load(self, mode, pointer):
        if mode == 1:
            load_pointer = pointer
        elif mode == 2:
            load_pointer = self.relative_base + self.state[pointer]
        else:
            load_pointer = self.state[pointer]

        if len(self.state) <= load_pointer:
            self.state.extend([0 for _ in range(load_pointer - len(self.state) + 1)])
        return self.state[load_pointer]

    def load_io(self, mode, pointer):
        if mode == 2:
            load_pointer = self.relative_base + self.state[pointer]
        else:
            load_pointer = self.state[pointer]

        if len(self.state) <= load_pointer:
            self.state.extend([0 for _ in range(load_pointer - len(self.state) + 1)])
        return load_pointer

    def store(self, pointer, value):
        if len(self.state) <= pointer:
            self.state.extend([0 for _ in range(pointer - len(self.state) + 1)])
        self.state[pointer] = value

    def run(self):
        self.running = True
        while self.running:
            self.step()

    def step(self):
        (ma, mb, mc, op) = self.decode_op(self.load(1, self.program_counter))
        if op == 1:  # add
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load_io(mc, self.program_counter + 3)  #
            self.store(c, a + b)  # Add
            self.program_counter += 4
        elif op == 2:  # mul
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load_io(mc, self.program_counter + 3)
            self.store(c, a * b)  # Multiply
            self.program_counter += 4
        elif op == 3:  # Interactive Input
            a = self.load_io(ma, self.program_counter + 1)

            if self.input_val is None:
                val = input("input>")
            else:
                if len(self.input_val) <= 0:
                    self.running = False
                    return
                val = self.input_val[0]
                self.input_val = self.input_val[1:]

            self.store(a, int(val))
            self.program_counter += 2
        elif op == 4:  # Output
            a = self.load_io(ma, self.program_counter + 1)
            # print(self.state[a])
            self.output.append(self.state[a])
            self.program_counter += 2
        elif op == 5:  # jmp if True
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            if a != 0:
                self.program_counter = b
            else:
                self.program_counter += 3
        elif op == 6:  # jmp if False
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            if a == 0:
                self.program_counter = b
            else:
                self.program_counter += 3
        elif op == 7:  # less-than
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load_io(mc, self.program_counter + 3)
            if a < b:
                self.store(c, 1)
            else:
                self.store(c, 0)
            self.program_counter += 4
        elif op == 8:  # equals
            a = self.load(ma, self.program_counter + 1)
            b = self.load(mb, self.program_counter + 2)
            c = self.load_io(mc, self.program_counter + 3)
            if a == b:
                self.store(c, 1)
            else:
                self.store(c, 0)
            self.program_counter += 4
        elif op == 9:  # Relative Base Offset
            # ma = 1
            a = self.load(ma, self.program_counter + 1)
            self.relative_base += a
            self.program_counter += 2
        elif op == 99:
            self.running = False
            self.completed = True
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
    comp = IntCode(prog)
    comp.run()
    print(comp.state)
    print(comp.output)
