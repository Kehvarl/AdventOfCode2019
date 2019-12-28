from IntCode import IntCode


# test_data = """..#..........
# ..#..........
# #######...###
# #.#...#...#.#
# #############
# ..#...#...#..
# ..#####...^..""".split("\n")


def parse_output(data):
    display = [chr(c) for c in data]
    return ("".join(display)).strip().split("\n")


def get_intersections(data):
    _intersections = []

    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if data[y][x] != ".":
                if data[y - 1][x] != "." and \
                        data[y + 1][x] != "." and \
                        data[y][x - 1] != "." and \
                        data[y][x + 1] != ".":
                    _intersections.append(x * y)
    return _intersections


def find_bot(data):
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if data[y][x] not in [".", "#"]:
                bot_pos = (x, y)
                bot = data[y][x]
                return bot_pos, bot


directions = {"^": (0, -1),
              ">": (1, 0),
              "v": (0, 1),
              "<": (-1, 0)}


def get_turn(data):
    bot_position, bot_direction = find_bot(data)
    x, y = bot_position

    dx, dy = (0, 0)
    for key in directions:
        cx, cy = directions[key]
        if key == bot_direction:
            continue
        if data[y + cy][x + cx] == "#":
            dx = cx
            dy = cy
            break

    return direction_to_turn(bot_direction, dx, dy)


def direction_to_turn(old_direction, dx, dy):
    if old_direction == "^":
        if dx == -1:
            return "L"
        elif dx == 1:
            return "R"
    elif old_direction == "v":
        if dx == 1:
            return "L"
        elif dx == -1:
            return "R"
    elif old_direction == "<":
        if dy == 1:
            return "L"
        elif dy == -1:
            return "R"
    elif old_direction == ">":
        if dy == -1:
            return "L"
        elif dy == 1:
            return "R"


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])
comp.run()

# intersections = get_intersections(parse_output(comp.output))
# print(intersections)
# print(sum(intersections))
# print("\n".join(parse_output(comp.output)))
print(get_turn(parse_output(comp.output)))
