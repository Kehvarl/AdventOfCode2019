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

turning = {"^": ["<", ">"],
           ">": ["^", "v"],
           "v": [">", "<"],
           "<": ["v", "^"]}


def get_turn(data, bx=None, by=None, bd=None):
    if bx is None:
        bot_position, bot_direction = find_bot(data)
        x, y = bot_position
    else:
        x = bx
        y = by
        bot_direction = bd

    dx, dy = (0, 0)
    new_direction = False
    for key in directions:
        cx, cy = directions[key]
        if key == bot_direction:
            continue
        if 0 <= y + cy < len(data) and 0 <= x + cx < len(data[0]) and data[y + cy][x + cx] == "#":
            dx = cx
            dy = cy
            new_direction = direction_to_turn(bot_direction, dx, dy)
            if new_direction:
                break

    return new_direction


def direction_to_turn(old_direction, dx, dy):
    if old_direction == "^":
        if dx == -1:
            return "L"
        elif dx == 1:
            return "R"
        else:
            return False
    elif old_direction == "v":
        if dx == 1:
            return "L"
        elif dx == -1:
            return "R"
        else:
            return False
    elif old_direction == "<":
        if dy == 1:
            return "L"
        elif dy == -1:
            return "R"
        else:
            return False
    elif old_direction == ">":
        if dy == -1:
            return "L"
        elif dy == 1:
            return "R"
        else:
            return False


def get_next_position(direction, bot_position):
    x, y = bot_position
    cx, cy = directions[direction]
    return x + cx, y + cy


comp = IntCode([int(x) for x in open("input.txt", "r").readline().split(",")])
comp.run()

# intersections = get_intersections(parse_output(comp.output))
# print(intersections)
# print(sum(intersections))
print("\n".join(parse_output(comp.output)))
# print(get_turn(parse_output(comp.output)))

scaffold = parse_output(comp.output)
pos, bot_direction = find_bot(scaffold)
bot_x, bot_y = pos

path = []
forward_count = 0
end = False

while not end:
    nx, ny = get_next_position(bot_direction, (bot_x, bot_y))

    if 0 <= ny < len(scaffold) and 0 <= nx < len(scaffold[0]) and scaffold[ny][nx] == "#":
        forward_count += 1
        bot_x, bot_y = nx, ny
    else:
        if forward_count > 0:
            path.append(forward_count)
            forward_count = 0
        turn = get_turn(scaffold, bot_x, bot_y, bot_direction)
        if turn == False:
            end = True
            break
        path.append(turn)
        bot_direction = turning[bot_direction][0 if turn == "L" else 1]

print(path)
# Can I move forward?  Increment forward count
# Else: Am I at the end? End
# Else: Turn
