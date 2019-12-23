from IntCode import IntCode

prog = [int(x) for x in open("input.txt", "r").readline().split(",")]

comps = [IntCode(prog, input_val=[x]) for x in range(50)]
idle = [False for x in range(50)]

for comp in comps:
    comp.run()  # Initialize

delivered_to_0 = []

nat = None
running = True
while running:
    for index in range(50):
        comp = comps[index]
        if len(comp.input_val) == 0:
            comp.input_val = [-1]
        comp.run()

        idle[index] = len(comp.output) == 0

        while len(comp.output) > 0:
            address = comp.output[0]
            x = comp.output[1]
            y = comp.output[2]
            comp.output = comp.output[3:]
            if address == 255:
                nat = (x, y)
            else:
                comps[address].input_val.extend([x, y])

    if all(i == True for i in idle):
        delivered_to_0.append(nat)
        x, y = nat
        comps[0].input_val = [x, y]
        if len(delivered_to_0) > 2 and delivered_to_0[-1] == delivered_to_0[-2]:
            print(nat)
            running = False
            break
