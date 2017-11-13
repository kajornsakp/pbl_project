from minutiae.minutiae import Minutiae

class FpMatcher(object):
    def __init__(self, fpSegmentator, fpEnhancer, mnExtractor, mnMatcher):
        self.fpSegmentator = fpSegmentator
        self.fpEnhancer = fpEnhancer
        self.mnExtractor = mnExtractor
        self.mnMatcher = mnMatcher

    def match(self, fpImg1, fpImg2):
        pass

