import cv2
import numpy as np
from minutiae.point2f import Point2f

class PointPair(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.d = None
        self.a = None

    def calEuclidDist(self):
        self.d = self.p.pos.getDistance(self.q.pos)

    def calAngle(self):
        ang2 = np.arctan2(self.p.pos.y, self.p.pos.x)
        ang1 = np.arctan2(self.q.pos.y, self.q.pos.x)
        self.a = np.rad2deg((ang1 - ang2) % (2 * np.pi))

    def __eq__(self, o: object) -> bool:
        return self.d == o.d

    def __lt__(self, other):
        return self.d < other.d

    def __str__(self):
        return "({}, {})\t\t{:.6f}\t\t{:.6f}".format(self.p, self.q, self.d, self.a)


class MnMatcher(object):
    def __calEuclidDistForSet(self, forSet):
        d = []
        n = len(forSet)
        for i in range(n):
            for j in range(i + 1, n):
                pair = PointPair(forSet[i], forSet[j])
                pair.calEuclidDist()
                pair.calAngle()
                d.append(pair)
        return d


    def __calEuclidDist(self, mnSet1, mnSet2):
        # mnSet1 = {mn1, mn2,...,mn_i} (i = len(mnSet))
        # p = mnSet1[0]
        # d = []
        # for i in range(1, len(mnSet1)):
        #     p_i = mnSet1[i]
        #     pair = PointPair(p, p_i)
        #     d.append(pair)
        #
        # q = mnSet2[0]
        # s = []
        # for j in range(1, len(mnSet2)):
        #     q_j = mnSet2[j]
        #     pair = PointPair(q, q_j)
        #     s.append(pair)

        # 1. calculate the Euclidean distance
        distSet1 = self.__calEuclidDistForSet(mnSet1)
        distSet2 = self.__calEuclidDistForSet(mnSet2)

        # 2. sort ascending order by distance
        distSet1 = sorted(distSet1)
        distSet2 = sorted(distSet2)

        return distSet1, distSet2

    def __recordMatchPoints(self, d1, d2):
        m, n = len(d1), len(d2)
        i, j = 1, 1
        matchedSet = []
        while True:
            if i == m or j == n:
                break

            if d1[i] == d2[j]:
                matchedSet.append((d1[i], d2[j]))
                i += 1
            elif d1[i] > d2[j]:
                j += 1
            elif d1[i] < d2[j]:
                i += 1

        return matchedSet

    def __computeCongruent(self):
        # 1. Select a pair of matched points p and q
        # 2. Calculate the distances from p and q to other corresponding matched points
        # 3. Compute the congruent complete graphs

        pass

    def __calAngle(self, p1, p2):
        ang2 = np.arctan2(p1.y, p1.x)
        ang1 = np.arctan2(p2.y, p2.x)
        return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    def angle_between(self, p1, p2):
        ang1 = np.arctan2(*p1[::-1])
        ang2 = np.arctan2(*p2[::-1])
        return (ang1 - ang2) % (2 * np.pi)
        # return np.rad2deg((ang1 - ang2) % (2 * np.pi))

    def match(self, mnSet1, mnSet2):


        # 1. calculate the Euclidean distance
        #       distSet: [ PointPair ]
        distSet1, distSet2 = self.__calEuclidDist(mnSet1, mnSet2)

        # 2. record the matched points
        #       matchedSet: [ tuple(distSet) ]
        matchedSet = self.__recordMatchPoints(distSet1, distSet2)

        # 3.


        # 3. select a pair of matched points
        c = 0

        for m in matchedSet:
            # print("p: {}\nq: {}".format(m[0], m[1]))
            # print('Soln')

            # A ======
            a1 = Point2f(m[0].p.pos.x, m[0].p.pos.y)
            a2 = Point2f(m[1].p.pos.x, m[1].p.pos.y)

            aDist = a1.getDistance(a2)
            #aAngle = self.__calAngle(a1, a2)
            # print("\tA: ", end='')
            # print(a1, a2, aDist)

            # B ======
            b1 = Point2f(m[0].q.pos.x, m[0].q.pos.y)
            b2 = Point2f(m[1].q.pos.x, m[1].q.pos.y)
            bDist = b1.getDistance(b2)
            #bAngle = self.__calAngle(b1, b2)

            # print("\tB: ", end='')
            # print(b1, b2, bDist)

            if aDist == 0 and bDist == 0:
                distRatio = 1
            else:
                dists = [aDist, bDist]
                distRatio = min(dists) / max(dists)

            # angleRatio = min(angles) / max(angles)
            # if angleRatio < 0.8:
            #     bAngle = self.__calAngle(b2, b1)
            #     angles = [aAngle, bAngle]
            #     angleRatio = min(angles) / max(angles)

            # set = [distRatio, angleRatio]
            # ratio = min(set) / max(set)
            #
            # print("\tDistance Ratio: ", distRatio)
            # print("\tAngle Ratio: ", angleRatio)
            # print("\tRatio: ", ratio)
            #
            if distRatio > 0.6:
                c += 1

            # if ratio > 0.9:
            #     c += 1
            # c += 1
            # if (c == 5):
            #     break
            # print('-----------------------------------'*2)
        print()
        print("======"*10)
        print("mnSet1={}, mnSet2={}, matchedSet={}".format(len(distSet1), len(distSet2), len(matchedSet)))

        lenDists = [len(distSet1), len(distSet2)]
        print("size ratio:", (min(lenDists) / max(lenDists)) * 100)

        print("Total match: ", c)

        # for i in range(len(d)):
        #     print("{} \t:\t {}".format(d[i], s[i]))


        # print(mnSet1[0].pos.getDistance(mnSet1[1].pos))
        # print(mnSet2[0].pos.getDistance(mnSet2[1].pos))

    def checkORB(self, keyPoint1, keyPoint2):

        img = cv2.imread('temp.png', 0)
        out = np.zeros(shape=(len(img), len(img)))
        orb = cv2.ORB_create()

        img2 = cv2.imread('temp.png', 0)
        out2 = np.zeros(shape=(len(img), len(img)))
        orb2 = cv2.ORB_create()


        # find the keypoints with ORB
        kp = orb.detect(img, None)
        kp2 = orb.detect(img2, None)
        # compute the descriptors with ORB
        kp, des = orb.compute(img, keyPoint1)
        kp2, des2 = orb.compute(img, keyPoint2)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        print(matches)
        print(self.evaluate(keyPoint1, matches, 50))
        img3 = cv2.drawMatches(img, kp, img2, kp2, matches, out, flags=2)


    def evaluate(self, inp1, matches, percentage):
        print((len(matches) / len(inp1)) * 100)
        if (len(inp1) < len(matches)):
            print("Something must be wrong!!!")
            return
        if ((len(matches) / len(inp1)) * 100 > percentage):
            return True
        return False

    def match2(self, mnSet1, mnSet2):
        self.checkORB(mnSet1, mnSet2)
