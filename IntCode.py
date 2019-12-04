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
        op = self.load(self.program_counter)
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
            self.error = True
            self.error_detail = "Invalid OpCode Encountered: {} at {}.".format(op, self.program_counter)
