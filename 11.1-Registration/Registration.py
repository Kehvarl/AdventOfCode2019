from IntCode import IntCode


class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.min_x = 0
        self.min_y = 0
        self.max_x = 0
        self.max_y = 0
        self.direction = 0
        self.grid = {}
        self.path = []
        self.painted = 0

    def paint(self, color):
        if 0 > color > 1:
            print(color)
        if (self.x, self.y) not in self.grid:
            self.painted += 1
        self.grid[(self.x, self.y)] = color
        self.path.append((self.x, self.y, color))

    def turn(self, direction):
        if 0 > direction > 1:
            print(direction)

        if direction == 0:
            self.direction -= 1
        else:
            self.direction += 1
        self.direction = self.direction % 4
        self.move()

    def move(self):
        if self.direction == 0:  # Up
            self.y -= 1
        elif self.direction == 1:  # Right
            self.x += 1
        elif self.direction == 2:  # Down
            self.y += 1
        elif self.direction == 3:  # Left
            self.x -= 1
        else:
            print("broken")

        if self.x < self.min_x:
            self.min_x = self.x
        if self.y < self.min_y:
            self.min_y = self.y
        if self.x > self.max_x:
            self.max_x = self.x
        if self.y > self.max_y:
            self.max_y = self.y

    def get_color(self):
        return self.grid.get((self.x, self.y), 0)


prog = [3, 8, 1005, 8, 361, 1106, 0, 11, 0, 0, 0, 104, 1, 104, 0, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0,
        8, 10, 4, 10, 1001, 8, 0, 28, 2, 1104, 18, 10, 1006, 0, 65, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108,
        1, 8, 10, 4, 10, 1001, 8, 0, 57, 1, 1101, 5, 10, 2, 108, 15, 10, 2, 102, 12, 10, 3, 8, 1002, 8, -1, 10, 101, 1,
        10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 102, 1, 8, 91, 2, 1005, 4, 10, 2, 1107, 10, 10, 1006, 0, 16, 2, 109, 19,
        10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 1, 10, 4, 10, 101, 0, 8, 129, 1, 104, 3, 10, 1,
        1008, 9, 10, 1006, 0, 65, 1, 104, 5, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10, 10, 4, 10, 108, 1, 8, 10, 4, 10,
        102, 1, 8, 165, 1, 1106, 11, 10, 1, 1106, 18, 10, 1, 8, 11, 10, 1, 4, 11, 10, 3, 8, 1002, 8, -1, 10, 101, 1, 10,
        10, 4, 10, 108, 1, 8, 10, 4, 10, 1001, 8, 0, 203, 2, 1003, 11, 10, 1, 1105, 13, 10, 1, 101, 13, 10, 3, 8, 102,
        -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 101, 0, 8, 237, 2, 7, 4, 10, 1006, 0, 73, 1, 1003, 7,
        10, 1006, 0, 44, 3, 8, 102, -1, 8, 10, 1001, 10, 1, 10, 4, 10, 108, 1, 8, 10, 4, 10, 101, 0, 8, 273, 2, 108, 14,
        10, 3, 8, 102, -1, 8, 10, 101, 1, 10, 10, 4, 10, 108, 0, 8, 10, 4, 10, 102, 1, 8, 299, 1, 1107, 6, 10, 1006, 0,
        85, 1, 1107, 20, 10, 1, 1008, 18, 10, 3, 8, 1002, 8, -1, 10, 1001, 10, 1, 10, 4, 10, 1008, 8, 0, 10, 4, 10,
        1001, 8, 0, 337, 2, 107, 18, 10, 101, 1, 9, 9, 1007, 9, 951, 10, 1005, 10, 15, 99, 109, 683, 104, 0, 104, 1,
        21102, 1, 825594852248, 1, 21101, 378, 0, 0, 1105, 1, 482, 21101, 0, 387240006552, 1, 21101, 0, 389, 0, 1106, 0,
        482, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0, 104, 1, 3, 10, 104, 0,
        104, 0, 3, 10, 104, 0, 104, 1, 21101, 0, 29032025091, 1, 21101, 436, 0, 0, 1106, 0, 482, 21101, 29033143299, 0,
        1, 21102, 1, 447, 0, 1105, 1, 482, 3, 10, 104, 0, 104, 0, 3, 10, 104, 0, 104, 0, 21101, 988669698916, 0, 1,
        21101, 0, 470, 0, 1106, 0, 482, 21101, 0, 709052072804, 1, 21102, 1, 481, 0, 1106, 0, 482, 99, 109, 2, 21202,
        -1, 1, 1, 21101, 0, 40, 2, 21101, 0, 513, 3, 21101, 503, 0, 0, 1106, 0, 546, 109, -2, 2105, 1, 0, 0, 1, 0, 0, 1,
        109, 2, 3, 10, 204, -1, 1001, 508, 509, 524, 4, 0, 1001, 508, 1, 508, 108, 4, 508, 10, 1006, 10, 540, 1101, 0,
        0, 508, 109, -2, 2105, 1, 0, 0, 109, 4, 1202, -1, 1, 545, 1207, -3, 0, 10, 1006, 10, 563, 21102, 0, 1, -3,
        21202, -3, 1, 1, 22101, 0, -2, 2, 21102, 1, 1, 3, 21101, 582, 0, 0, 1105, 1, 587, 109, -4, 2106, 0, 0, 109, 5,
        1207, -3, 1, 10, 1006, 10, 610, 2207, -4, -2, 10, 1006, 10, 610, 21202, -4, 1, -4, 1106, 0, 678, 22102, 1, -4,
        1, 21201, -3, -1, 2, 21202, -2, 2, 3, 21102, 629, 1, 0, 1106, 0, 587, 22102, 1, 1, -4, 21101, 0, 1, -1, 2207,
        -4, -2, 10, 1006, 10, 648, 21102, 0, 1, -1, 22202, -2, -1, -2, 2107, 0, -3, 10, 1006, 10, 670, 21202, -1, 1, 1,
        21101, 670, 0, 0, 105, 1, 545, 21202, -2, -1, -2, 22201, -4, -2, -4, 109, -5, 2106, 0, 0]

robot = Robot()
comp = IntCode(prog, input_val=[1])
comp.run()
# Interpreter always returns 8,3 for first output.  Should be 1,0
print(comp.state[comp.output.pop()])
print(comp.state[comp.output.pop()])
robot.paint(1)
robot.turn(1)


while not comp.completed:
    color = robot.get_color()
    comp.input_val.append(color)
    comp.run()
    # print(comp.output)
    comp.output.reverse()
    robot.paint(comp.output.pop())
    robot.turn(comp.output.pop())

print(robot.painted)
# print(robot.grid)
# print(len(robot.grid.keys()))
print(robot.min_x, robot.min_y)
print(robot.max_x, robot.max_y)


for y in range(robot.min_y, robot.max_y + 1):
    line = ""
    for x in range(robot.min_x, robot.max_x + 1):
        line += ("00" if (robot.grid.get((x, y), 0) == 1) else "  ") + "."
    print(line)

print(len(robot.path))
print(robot.path)
