

class MnMatcher(object):
    @staticmethod
    def match(mnSet1, mnSet2):
        print(mnSet1[0].pos.getDistance(mnSet1[1].pos))
        print(mnSet2[0].pos.getDistance(mnSet2[1].pos))



