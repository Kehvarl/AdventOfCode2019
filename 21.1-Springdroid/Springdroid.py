from IntCode import IntCode


def send_instructions(instructions, computer):
    for instruction in instructions:
        operation = [ord(char) for char in instruction]
        operation.append(10)
        comp.input_val = operation
        comp.run()


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")], input_val=[])
comp.run()

prog = ["NOT A J",  # Hole in A

        "NOT B T",  # Or in B
        "OR T J",

        "NOT C T",  # Or in C
        "OR T J",

        "AND D J",  # only if Safe landing in D

        "NOT E T",  # Hole in E
        "NOT T T",  # Actually Not a hole in E (Can walk to)

        "OR H T",  # Or not a hole in H (Can Jump to)

        "AND T J",  # Need to jump soon. AND safe landing spot, and somewhere to go afterwords.

        "RUN"]

send_instructions(prog, comp)

# out = [chr(char) for char in comp.output]
print(comp.output)
#print("".join(out))
