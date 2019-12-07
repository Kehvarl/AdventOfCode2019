from collections import deque


class Orbit:
    def __init__(self):
        self.orbits = {}

    def populate_orbits(self, input):
        for orbit in input.strip().split("\n"):
            a, b = orbit.split(')')
            if self.orbits.get(a, False):
                self.orbits[a].append(b)
            else:
                self.orbits[a] = [b]

    def orbit_counts(self):
        count = 0
        for mass in self.orbits.keys():
            count += self.count_orbiting(mass) - 1
        return count

    def count_orbiting(self, start):
        satellites = self.orbits.get(start, False)
        count = 1
        if satellites:
            for s in satellites:
                count += self.count_orbiting(s)

        return count

    def find_path(self, start="YOU", end="SAN", transfers=[]):
        transfers = transfers + [start]
        if start == end:
            return transfers
        if self.orbits.get(start, False):
            for node in self.orbits[start]:
                if node not in transfers:
                    newpath = self.find_path(node, end, transfers)
                    if newpath:
                        return newpath
        return None

    def orbiting(self, subject):
        for mass in self.orbits.keys():
            if subject in self.orbits[mass]:
                return mass

    def orbit_transfers(self, subject, transfers=None):
        if transfers is None: transfers = []
        transfers.append(subject)
        if subject != "COM":
            return self.orbit_transfers(self.orbiting(subject), transfers)
        else:
            return transfers

    def transfers_needed(self, start, end):
        orbits_start = self.orbit_transfers(start)
        orbits_end = self.orbit_transfers(end)
        transfers = []
        overlap = False
        for t in orbits_start:
            if t == start or t == end:
                continue
            else:
                if t not in orbits_end and overlap == False:
                    transfers.append(t)
                elif overlap == False:
                    transfers.append(t)
                    overlap = True

        orbits_end.reverse()
        for t in orbits_end:
            if t == start or t == end:
                continue
            else:
                if t not in orbits_start:
                    transfers.append(t)

        return transfers


if __name__ == "__main__":
    map = Orbit()
    data = open("input.txt", 'r').read()
    map.populate_orbits(data)
    print(map.orbits)
    print(map.orbit_counts())
    youpath = map.orbit_transfers("YOU")
    sanpath = map.orbit_transfers("SAN")
    print(youpath)
    print(sanpath)
    print(map.transfers_needed("YOU", "SAN"))
    print(len(map.transfers_needed("YOU", "SAN")) - 1)
