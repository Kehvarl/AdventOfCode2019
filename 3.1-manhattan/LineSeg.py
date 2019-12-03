class LineSeg:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

        if x1 == x2:
            self.axis = "x"
            self.axis_val = x1
            self.start = min(y1, y2)
            self.end = max(y1, y2)
        elif y1 == y2:
            self.axis = "y"
            self.axis_val = y1
            self.start = min(x1, x2)
            self.end = max(x1, x2)
        else:
            raise Exception()

    def intersect(self, other):
        if self.axis == other.axis:
            return False

        if other.start < self.axis_val < other.end:
            if self.axis == "x":
                return (self.axis_val, other.axis_val)
            else:
                return (other.axis_val, self.axis_val)
        else:
            return False


if __name__ == "__MAIN__":
    A = Line(-30, 0, 30, 0)
    B = Line(5, 15, 5, -15)

    print(A.intersect(B))
