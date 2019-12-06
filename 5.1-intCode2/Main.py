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
        opcode = str(opcode)
        if len(opcode) < 5:
            a = 0
        else:
            a = opcode[0]
        if len(opcode) < 4:
            b = 0
        else:
            b = opcode[-4:1]
        if len(opcode) < 3:
            c = 0
        else:
            c = opcode[-3:2]
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
            val = int(input())
            self.store(a, val)
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



def main():
    # print (int_code ([1,9,10,3,2,3,11,0,99,30,40,50]))
    # print (int_code([1,0,0,0,99]))
    # prog = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
    # prog = [3,0,4,0,99]
    prog = [1002,4,3,4,33]
    comp = IntCode(prog)
    comp.run()
    # test

main()
