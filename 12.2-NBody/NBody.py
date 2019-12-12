class Moon:
    def __init__(self, x, y, z, vx=0, vy=0, vz=0):
        self.x = x
        self.y = y
        self.z = z

        self.vx = vx
        self.vy = vy
        self.vz = vz

    def tick(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kinetic_energy(self):
        return abs(self.vx) + abs(self.vy) + abs(self.vz)

    def total_energy(self):
        return self.potential_energy() * self.kinetic_energy()

    def __repr__(self):
        return "pos=<x= {}, y= {}, z= {}>, vel=<x= {}, y= {}, z= {}".format(self.x, self.y, self.z, self.vx, self.vy,
                                                                            self.vz)

    @staticmethod
    def apply_gravity(a, b):
        if a.x > b.x:
            a.vx -= 1
            b.vx += 1
        elif a.x < b.x:
            a.vx += 1
            b.vx -= 1

        if a.y > b.y:
            a.vy -= 1
            b.vy += 1
        elif a.y < b.y:
            a.vy += 1
            b.vy -= 1

        if a.z > b.z:
            a.vz -= 1
            b.vz += 1
        elif a.z < b.z:
            a.vz += 1
            b.vz -= 1


if __name__ == "__main__":
    # moons = [Moon(-1, 0, 2),Moon(2, -10, -7),Moon(4, -8, 8),Moon(3, 5, -1)]
    # moons = [Moon(-8, -10, 0),Moon(5, 5, 10),Moon(2, -7, 3),Moon(9, -8, -3)]
    # < x = -5, y = 6, z = -11 >
    # < x = -8, y = -4, z = -2 >
    # < x = 1, y = 16, z = 4 >
    # < x = 11, y = 11, z = -4 >
    moons = [Moon(-5, 6, -11), Moon(-8, -4, -2), Moon(1, 16, 4), Moon(11, 11, -4)]

    pairs = [(0, 1), (0, 2), (0, 3),
             (1, 2), (1, 3),
             (2, 3)]

    for moon in moons:
        print(moon)

    for i in range(1000):
        for pair in pairs:
            a, b = pair
            Moon.apply_gravity(moons[a], moons[b])

        for moon in moons:
            moon.tick()

    print()
    TE = 0
    for moon in moons:
        print(moon)
        print(moon.total_energy())
        TE += moon.total_energy()

    print(TE)
