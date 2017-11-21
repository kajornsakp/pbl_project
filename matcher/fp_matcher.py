import cv2
import numpy as np
import scipy.ndimage as ndimage
import segment
import enhancer
import extractor

from .mn_matcher import MnMatcher

class FpMatcher(object):
    def __getMnSet(self, img_src):
        np.set_printoptions(
            threshold=np.inf,
            precision=4,
            suppress=True)

        # sourceImage = './asset/102_3.tif'

        # Reading image
        image = ndimage.imread(img_src, mode="L").astype("float64")

        # segement
        image, mask = segment.findMask(image)

        #enhancer
        image = enhancer.enhancer(image, mask)

        #extrator
        image = extractor.extractor(image, mask)

        return image

    def match(self, img_src_1, img_src_2):

        # mnSet1, img1 = self.__getMnSet(img_src_1)
        # mnSet2, img2 = self.__getMnSet(img_src_2)

        mnSet1 = self.__getMnSet(img_src_1)
        mnSet2 = self.__getMnSet(img_src_2)


        lenDists = [len(mnSet1), len(mnSet2)]
        ratio = (min(lenDists) / max(lenDists)) * 100
        if ratio < 70:
            return 0

        mnMatcher = MnMatcher()
        mnMatcher.match(mnSet1, mnSet2)

        cv2.waitKey()


        print("done getting mnSet")

