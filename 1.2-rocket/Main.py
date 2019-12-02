def calc_fuel(mass):
    fuel_needed = (mass // 3) - 2

    if fuel_needed > 0:
        return fuel_needed + calc_fuel(fuel_needed)
    else:
        return 0


def main():
    module_data = open("input.txt", "r")
    modules = []

    for m in module_data:
        if int(m):
            modules.append(calc_fuel(int(m)))

    print(sum(modules))


main()
