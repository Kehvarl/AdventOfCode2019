from IntCode import IntCode

comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")], input_val=[])
while True:
    comp.run()

    out = [chr(char) for char in comp.output]
    print(comp.output)
    print("".join(out))
    command = input("command: ")
    operation = [ord(char) for char in command]
    operation.append(10)
    comp.input_val = operation
