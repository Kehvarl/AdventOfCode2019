import collections

neighbors = [(0, -1), (-1, 0), (1, 0), (0, 1)]


# Sohpie Alpert's implementation
# Copied from https://github.com/sophiebits/adventofcode/blob/master/2019/day18.py
def bfs_search(grid, start, havekeys):
    heignt = len(grid)
    width = len(grid[0])

    to_search = collections.deque([start])
    distances = {start: 0}
    keys_collected = {}

    while to_search:
        pt = to_search.popleft()

        for neighbor in neighbors:
            nx = pt[0] + neighbor[0]
            ny = pt[1] + neighbor[1]

            if not 0 <= ny < heignt and 0 <= nx < width:
                continue

            tile = grid[ny][nx]

            if tile.isalpha() and tile.isupper() and tile.lower() not in havekeys:
                continue

            if tile.isalpha() and tile.islower and tile not in havekeys:
                keys_collected[tile] = distances[(nx, ny)], (nx, ny)
            else:
                to_search.append((nx, ny))
    return keys_collected


seen = {}


def minwalk(grid, starts, havekeys):
    hks = ''.join(sorted(havekeys))
    if (starts, hks) in seen:
        return seen[starts, hks]
    if len(seen) % 10 == 0:
        print(hks)
    keys = bfs_search(grid, starts, havekeys)
    if len(keys) == 0:
        # done!
        ans = 0
    else:
        poss = []
        for ch, (dist, pt, roi) in keys.items():
            nstarts = tuple(pt if i == roi else p for i, p in enumerate(starts))
            poss.append(dist + minwalk(grid, nstarts, havekeys + ch))
        ans = min(poss)
    seen[starts, hks] = ans
    return ans


maze = """########################
#f.D.E.e.C.b.A.@.a.B.c.#
######################.#
#d.....................#
########################""".split("\n")

starts = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '@':
            starts.append((i, j))

print(minwalk(maze, starts, ''))
