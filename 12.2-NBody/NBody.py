from math import gcd
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

    def state(self):
        return [self.x, self.y, self.z, self.vx, self.vy, self.vz]

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

    x_ = []
    y_ = []
    z_ = []
    repeat_x = None
    repeat_y = None
    repeat_z = None
    loop_count = 0

    while repeat_x is None or repeat_y is None or repeat_z is None:
        for pair in pairs:
            a, b = pair
            Moon.apply_gravity(moons[a], moons[b])

        x_state = ""
        y_state = ""
        z_state = ""
        for moon in moons:
            moon.tick()
            x_state += str(moon.x) + str(moon.vx)
            y_state += str(moon.y) + str(moon.vy)
            z_state += str(moon.z) + str(moon.vz)

        if x_state not in x_:
            x_.append(x_state)
        elif repeat_x is None:
            repeat_x = loop_count

        if y_state not in y_:
            y_.append(y_state)
        elif repeat_y is None:
            repeat_y = loop_count

        if z_state not in z_:
            z_.append(z_state)
        elif repeat_z is None:
            repeat_z = loop_count

        loop_count += 1

    print(repeat_x, repeat_y, repeat_z)


    def least_common_multiple(x, y):
        return x // gcd(x, y) * y


    print(least_common_multiple(least_common_multiple(repeat_x, repeat_y), repeat_z))
