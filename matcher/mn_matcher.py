class PointPair(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.d = None

    def calEuclidDist(self):
        self.d = self.p.pos.getDistance(self.q.pos)

    def __eq__(self, o: object) -> bool:
        return self.d == o.d

    def __lt__(self, other):
        return self.d < other.d

    def __str__(self):
        return "({}, {}):{}".format(self.p, self.q, self.d)


class MnMatcher(object):
    def __calEuclidDistForSet(self, forSet):
        d = []
        n = len(forSet)
        for i in range(n):
            for j in range(i + 1, n):
                pair = PointPair(forSet[i], forSet[j])
                pair.calEuclidDist()
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


    def match(self, mnSet1, mnSet2):
        # 1. calculate the Euclidean distance
        distSet1, distSet2 = self.__calEuclidDist(mnSet1, mnSet2)

        # 2. record the matched points
        # matchedSet = self.__recordMatchPoints(distSet1, distSet2)

        # 3. select a pair of matched points
        # for m in matchedSet:
            # print("{} == {}".format(m[0], m[1]))

        # for i in range(len(d)):
        #     print("{} \t:\t {}".format(d[i], s[i]))



        # print(mnSet1[0].pos.getDistance(mnSet1[1].pos))
        # print(mnSet2[0].pos.getDistance(mnSet2[1].pos))



