from IntCode import IntCode


def send_instructions(instructions, computer):
    for instruction in instructions:
        operation = [ord(char) for char in instruction]
        operation.append(10)
        comp.input_val = operation
        comp.run()


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")], input_val=[])
comp.run()

prog = ["NOT A J",
        "NOT B T",
        "OR T J",
        "NOT C T",
        "OR T J",
        "AND D J",
        "WALK"]

send_instructions(prog, comp)

# out = [chr(char) for char in comp.output]
print(comp.output)
# print("".join(out))
