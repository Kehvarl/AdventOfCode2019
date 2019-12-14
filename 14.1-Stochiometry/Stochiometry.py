input = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

reactions = {}
for line in input.split("\n"):
    raw, product = line.split(" => ")
    pqty, prod = product.split(" ")
    raw_m = raw.split(",")
    raw_list = []
    for mat in raw_m:
        qty, mat1 = mat.strip().split(" ")
        raw_list.append((mat1, qty))

    reactions[(prod)] = (raw_list[:], pqty)

print(reactions)

extra = {}

def needed_for(qty, material):
    needed_materials, makes = reactions[(material)]

    out = 0
    for precursor, needed in needed_materials:
        needed = int(needed)
        if precursor in extra:
            if extra[precursor] >= needed:
                extra[precursor] -= needed
                needed = 0
            else:
                needed -= extra[precursor]
                extra[precursor] = 0

        # ratio = int(needed) // int(makes)
        if needed > 0:
            if precursor == "ORE":
                out += needed
            else:
                out += needed_for(int(qty), precursor)
    return out


print(needed_for(1, "FUEL"))
