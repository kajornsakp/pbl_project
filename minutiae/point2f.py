import math

class Point2f:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getDistance(self, o):
        return math.sqrt((o.x - self.x)**2 + (o.y - self.y)**2)