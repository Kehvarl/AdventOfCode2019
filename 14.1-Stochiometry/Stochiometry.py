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

materials = {}


def needed_for(qty, material):
    needed_materials, makes = reactions[(material)]

    for precursor, needed in needed_materials:
        if precursor == "ORE":
            out = int(needed)
        else:
            out = needed_for(int(needed) * qty, precursor)

    return out


print(needed_for(1, "FUEL"))
