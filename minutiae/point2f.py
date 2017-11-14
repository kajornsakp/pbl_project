import math

class Point2f:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getDistance(self, o):
        d = math.sqrt((o.x - self.x)**2 + (o.y - self.y)**2)
        return float("{0:.6f}".format(d))

    def __str__(self):
        return "({}, {})".format(self.x, self.y)