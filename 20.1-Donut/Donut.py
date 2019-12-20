example1 = """         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z       """

grid = [[val for val in line] for line in example1.split("\n")]
scanned = []


def check_adjacent(x, y, portal_id):
    for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y + _y > len(grid) - 1 or x + _x > len(grid[0]) - 1:
            continue

        if grid[y + _y][x + _x] == "." and len(portal_id) == 2:
            return x + _x, y + _y, portal_id

        elif grid[y + _y][x + _x].isalpha() and len(portal_id) == 1:
            return check_adjacent(x + _x, y + _y, portal_id + grid[y + _y][x + _x])

    return x, y, None


def in_portals(x, y):
    for portal in portals:
        for side in portals[portal]:
            _x, _y = side
            if (x, y) == (_x, _y):
                return _x, _y
    return False


portals = {}

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x].isalpha():
            _x, _y, portal = check_adjacent(x, y, grid[y][x])
            if portal is not None:
                portal = "".join(sorted(portal))
                if portals.get(portal):
                    portals[portal].append((_x, _y))
                else:
                    portals[portal] = [(_x, _y)]

print(portals)

x, y = portals["AA"][0]
path = [(x, y)]
done = False

while not done:
    for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if y + _y > len(grid) - 1 or x + _x > len(grid[0]) - 1:
            continue

        if grid[y + _y][x + _x] == "." and (x, y) not in path:
            x, y = [y + _y][x + _x]
            path.append((x, y))

        if in_portals(x, y):
            if (x, y) == portals["AA"][0]:
                continue
            elif (x, y) == portals["ZZ"][0]:
                done = True
                break
            x, y = in_portals(x, y)
            path.append((x, y))

print(path)
