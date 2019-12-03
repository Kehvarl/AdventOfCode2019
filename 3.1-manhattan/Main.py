def path_parser(path_string):
    points = [(0, 0)]
    prev = (0, 0)
    path = path_string.split(",")
    for val in path:
        command = val[0:1]
        distance = int(val[1:])
        x, y = prev
        if command == "R":
            x += distance
        elif command == "L":
            x -= distance
        elif command == "U":
            y += distance
        elif command == "D":
            y -= distance
        prev = (x, y)
        points.append(prev)

    return points


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return 0, 0

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return (int(x), int(y))


def manhattan(point):
    x, y = point
    return abs(x) + abs(y)


path1 = path_parser("R75,D30,R83,U83,L12,D49,R71,U7,L72")
path2 = path_parser("U62,R66,U55,R34,D71,R55,D58,R83")

# path1 = path_parser("R8,U5,L5,D3")
# path2 = path_parser("U7,R6,D4,L4")
intersect = []
for i in range(0, len(path1) - 1):
    p1x, p1y = path1[i]
    p2x, p2y = path1[i + 1]
    line1 = ([p1x, p1y], [p2x, p2y])
    for j in range(0, len(path2) - 1):
        q1x, q1y = path2[i]
        q2x, q2y = path2[j + 1]
        line2 = ([q1x, q1y], [q2x, q2y])
        print(line1, line2, line_intersection(line1, line2))
        intersect.append(line_intersection(line1, line2))

dist = []
for point in intersect:
    if point != (0, 0):
        dist.append(manhattan(point))

print(path1)
print(path2)
print(intersect)
print(min(dist))
