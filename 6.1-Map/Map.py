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
            count += self.orbiting(mass) - 1
        return count

    def orbiting(self, start):
        satellites = self.orbits.get(start, False)
        count = 1
        if satellites:

            for s in satellites:
                count += self.orbiting(s)

        return count


if __name__ == "__main__":
    map = Orbit()
    data = open("input.txt", 'r').read()
    map.populate_orbits(data)
    print(map.orbit_counts())
    print(map.orbiting("COM"))
print(map.orbits)
