def main():
    module_data = open("input.txt", "r")
    modules = []

    for m in module_data:
        print(m)
        print((int(m) // 3) - 2)
        modules.append((int(m) // 3) - 2)

    print(sum(modules))


main()
