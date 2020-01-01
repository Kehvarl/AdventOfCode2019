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

        h = to_search.popleft()
        for ne in neighbors:
            pt = (h[0] + ne[0], h[1] + ne[1])

            if not (0 <= pt[0] < len(grid) and 0 <= pt[1] < len(grid[0])):
                continue

            tile = grid[pt[0]][pt[1]]

            if tile == '#':
                continue
            if pt in distances:
                continue

            distances[pt] = distances[h] + 1
            if tile.isalpha() and tile.isupper() and tile.lower() not in havekeys:
                continue

            if tile.isalpha() and tile.islower() and tile not in havekeys:
                keys_collected[tile] = distances[pt], pt
            else:
                to_search.append(pt)

    return keys_collected


def reachablekeys(grid, start, havekeys):
    bfs = collections.deque([start])
    distance = {start: 0}
    keys = {}
    while bfs:
        h = bfs.popleft()
        for pt in [
            (h[0] + 1, h[1]),
            (h[0] - 1, h[1]),
            (h[0], h[1] + 1),
            (h[0], h[1] - 1),
        ]:
            if not (0 <= pt[0] < len(grid) and 0 <= pt[1] < len(grid[0])):
                continue
            ch = grid[pt[0]][pt[1]]
            if ch == '#':
                continue
            if pt in distance:
                continue
            distance[pt] = distance[h] + 1
            if 'A' <= ch <= 'Z' and ch.lower() not in havekeys:
                continue
            if 'a' <= ch <= 'z' and ch not in havekeys:
                keys[ch] = distance[pt], pt
            else:
                bfs.append(pt)
    return keys


seen = {}


def minwalk(grid, starts, havekeys):
    keys = {}
    hks = ''.join(sorted(havekeys))
    if (starts, hks) in seen:
        return seen[starts, hks]
    if len(seen) % 10 == 0:
        print(hks)
    for i, start in enumerate(starts):
        for ch, (dist, pt) in bfs_search(grid, start, havekeys).items():
            keys[ch] = dist, pt, i
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

maze = open("input.txt", "r").read().split("\n")

starts = []
for i in range(len(maze)):
    for j in range(len(maze[0])):
        if maze[i][j] == '@':
            starts.append((i, j))

print(minwalk(maze, tuple(starts), ''))
