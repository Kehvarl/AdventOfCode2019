class NanoAssembler:
    def __init__(self):
        self.reactions = {}
        self.available_materials = {}
        self.consumed_raw = {}

    def load_reactions(self, reactions_data):
        for line in reactions_data.split("\n"):
            raw, product = line.split("=>")
            prod_qty, prod = product.strip().split(" ")
            raw_m = raw.split(",")
            raw_list = []
            for mat in raw_m:
                qty, mat1 = mat.strip().split(" ")
                raw_list.append((mat1, qty))

            self.reactions[prod] = (raw_list[:], prod_qty)

    def craft(self, material, multiplier=1):
        recipe = self.reactions.get(material)

        if recipe:
            precursors, makes = recipe
            makes = int(makes)

            for ingredient, qty in precursors:
                qty = int(qty)

                if not self.available_materials.get(ingredient):
                    self.available_materials[ingredient] = 0

                while self.available_materials[ingredient] < (qty * multiplier):
                    produced = self.craft(ingredient, multiplier)

                    if not produced:  # can't craft, must be a raw material
                        if self.consumed_raw.get(ingredient):
                            self.consumed_raw[ingredient] += (qty * multiplier)
                            self.available_materials[ingredient] += (qty * multiplier)
                        else:
                            self.consumed_raw[ingredient] = (qty * multiplier)
                            self.available_materials[ingredient] += (qty * multiplier)
                        break

                self.available_materials[ingredient] -= (qty * multiplier)

            if not self.available_materials.get(material):
                self.available_materials[material] = 0
            self.available_materials[material] += (makes * multiplier)

            return True
        else:
            return False


input_recipe1 = """10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL"""

input_recipe2 = """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL"""

input_recipe3 = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""

input_recipe4 = """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF"""

input_recipe5 = """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX"""

puzzle_recipe = """10 LSZLT, 29 XQJK => 4 BMRQJ
22 HCKS => 1 GQKCZ
1 HCKS, 8 WZWRV, 18 HVZR => 7 BGFR
1 LSZLT, 1 WRKJ, 3 LJFP, 3 RNLPB, 1 NZGK, 3 LDSV, 5 RJDN, 8 HGFGC => 3 QZTXD
1 BRSGQ, 1 XGLF, 1 ZHSK, 20 LSZLT, 16 WFCPT, 3 KTWV, 1 QRJC => 4 XPKX
1 DCLR, 6 RNLPB => 5 HCKS
1 HFHFV => 3 SHLMF
2 LTMZQ, 21 FGCXN => 6 QKFKV
3 BGFR => 7 WRKJ
3 KHSB => 2 XQJL
3 SHLMF => 2 LPLG
12 SVHWT, 20 BXPSZ => 9 NBMF
2 FGCXN, 32 DCSVN => 8 TBDWZ
1 KHSB, 3 HGFGC => 6 WZWRV
27 WFCPT, 4 KTWV, 14 BRSGQ, 1 MFNK, 1 WRKJ, 2 NZGK, 24 FBFLK => 5 TRLCK
2 SVHWT => 3 QRJC
1 MNVR, 1 FKBMW => 2 FGCXN
4 GJXW => 9 JXFS
3 XQJK => 5 WNJM
1 WZVWZ, 1 XQJL => 9 SHKJV
2 DCSVN => 4 HDVC
2 GJXW => 2 RNLPB
1 QKFKV, 1 PBRWB => 5 WTZQ
14 QKFKV => 6 RDFTD
166 ORE => 1 QDSXV
2 DCSVN => 5 BXPSZ
113 ORE => 6 LTMZQ
13 MNVR => 7 RJDN
2 NZGK, 9 XQJK, 18 WRKJ => 9 KTWV
1 NZGK => 8 XQJK
6 RZCGN, 6 HDVC, 1 DLKR => 9 DSLXW
18 HVZR => 8 LJFP
7 XQJL => 1 NPDS
15 DLKR, 1 DSLXW, 26 MJFVP => 3 FBFLK
125 ORE => 9 MNVR
3 RJDN => 4 HFHFV
1 TBDWZ, 1 DCLR => 2 HVZR
2 SHKJV => 5 GJXW
7 LTMZQ, 1 QDSXV, 1 FKBMW => 3 DCSVN
9 LPLG, 11 JXFS => 3 BRSGQ
5 JXFS, 1 ZHSK, 25 XGLF => 4 MFNK
5 PBRWB => 2 SVHWT
15 SHKJV => 5 XGLF
1 XQJL, 2 NPDS => 4 DLKR
39 JXFS => 5 KSHF
6 GJXW, 1 FBFLK => 7 HGFGC
3 JXFS => 1 LSZLT
3 NBMF, 1 BMRQJ => 2 LDSV
1 JXFS, 25 GJXW, 10 HGFGC => 4 NZGK
8 QZTXD, 26 KSHF, 60 WNJM, 6 GJXW, 9 TRLCK, 20 XPKX, 21 FGCXN, 57 GQKCZ, 6 WRKJ => 1 FUEL
4 SVHWT, 1 RZCGN => 3 ZHSK
1 BXPSZ => 7 DCLR
8 RDFTD, 1 SHKJV, 1 HFHFV => 6 MJFVP
1 LTMZQ => 9 KHSB
5 WTZQ, 4 HGFGC, 4 HCKS => 9 WFCPT
184 ORE => 4 FKBMW
4 XQJL => 3 WZVWZ
12 QDSXV => 9 RZCGN
1 FBFLK, 7 HVZR => 9 PBRWB"""

fuel = 2959788
assembler = NanoAssembler()
assembler.load_reactions(puzzle_recipe)
assembler.craft("FUEL", fuel)

print(assembler.consumed_raw)
print(assembler.available_materials)
print(fuel)
print(1000000000000 - assembler.consumed_raw["ORE"])
