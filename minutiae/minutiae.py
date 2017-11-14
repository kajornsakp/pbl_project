from enum import Enum


class MType(Enum):
    UNKNOWN = 0
    ENDPOINT = 1
    BIFURCATION = 2


class Minutiae:
    def __init__(self, posVal, typeVal = MType.UNKNOWN):
        self.pos = posVal       # Point2f
        self.type = typeVal     # MType

    def __str__(self):
        return "{}".format(self.pos)
