import math
import cv2
import numpy as np
from minutiae.minutiae import Minutiae, MType
from minutiae.point2f import Point2f
from matcher. mn_matcher import MnMatcher
import random as rand


def rotatePoint(centerPoint, point, angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(angle)
    r = (point[0] - centerPoint[0],
         point[1] - centerPoint[1])
    r = (r[0] * math.cos(angle) - r[1] * math.sin(angle),
         r[0] * math.sin(angle) + r[1] * math.cos(angle))
    r = (r[0] + centerPoint[0],
         r[1] + centerPoint[1])
    return r


if __name__ == '__main__':
    # start random points
    w, h = 600, 600
    n = 400

    mnSet1 = []
    mTypes = [MType.ENDPOINT, MType.BIFURCATION]
    for i in range(n):
        x = rand.randint(100, w - 100)
        y = rand.randint(100, h - 100)

        posVal = Point2f(x, y)
        mType = mTypes[rand.randint(0, 1)]

        mnSet1.append(Minutiae(posVal, mType))

    mnSet2 = []
    centerPoint = (w/2, h/2)
    for i in range(n):
        point = (mnSet1[i].pos.x, mnSet1[i].pos.y)
        x, y = rotatePoint(centerPoint, point, 30)

        print(x, y)

        posVal = Point2f(int(x), int(y))
        mType = mTypes[rand.randint(0, 1)]

        mnSet2.append(Minutiae(posVal, mType))

    img1 = np.zeros((w, h), np.uint8)
    for mn in mnSet1:
        img1[mn.pos.x, mn.pos.y] = 255

    img2 = np.zeros((w, h), np.uint8)
    for mn in mnSet2:
        img2[mn.pos.x, mn.pos.y] = 255

    MnMatcher.match(mnSet1, mnSet2)

    cv2.imshow('original', img1)
    cv2.imshow('rotated', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()