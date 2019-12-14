input_recipe = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""


def parse_recipe(recipe):
    reactions = {}

    for line in recipe.split("\n"):
        raw, product = line.split(" => ")
        prod_qty, prod = product.split(" ")
        raw_m = raw.split(",")
        raw_list = []
        for mat in raw_m:
            qty, mat1 = mat.strip().split(" ")
            raw_list.append((mat1, qty))

        reactions[prod] = (raw_list[:], prod_qty)

    return reactions


def needed_for(qty, material, reactions):
    needed_materials, makes = reactions[material]
    return 0


recipe_data = parse_recipe(input_recipe)
print(recipe_data)

print(needed_for(1, "FUEL", recipe_data))
