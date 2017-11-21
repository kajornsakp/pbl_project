import cv2
import numpy as np
import scipy.misc as misc
import scipy.ndimage as ndimage
import utils.utils as utils
from utils.gabor import gaborFilter


from extractor.skeletonizer import Skeletonizer
from extractor.mn_extractor import MnExtractor
from .mn_matcher import MnMatcher
from minutiae import minutiae

class FpMatcher(object):
    def __getMnSet(self, image):
        np.set_printoptions(
            threshold=np.inf,
            precision=4,
            suppress=True)

        # sourceImage = './asset/102_3.tif'

        # Reading image
        # image = ndimage.imread(img_src, mode="L").astype("float64")

        # Normalizing
        image = utils.normalize(image)

        # Finding mask
        mask = utils.findMask(image)

        # Applying local normalization
        image = np.where(mask == 1.0, utils.localNormalize(image), image)

        # Estimating orientations
        orientations = np.where(mask == 1.0, utils.estimateOrientations(image), -1.0)
        utils.showOrientations(image, orientations, "orientations", 8)

        # Estimating frequencies
        frequencies = np.where(mask == 1.0, utils.estimateFrequencies(image, orientations), -1.0)

        # Filtering
        image = gaborFilter(image, orientations, frequencies)

        # Binarizing
        image = np.where(mask == 1.0, utils.binarize(image), 1.0)
        misc.imsave('temp.png', image)
        image = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)

        # Skeletonizer
        ske_img = Skeletonizer.skeletonize(image)

        # Extract minutiae
        return MnExtractor.extract(ske_img), ske_img

    def match(self, img_src_1, img_src_2):
        img_src_1 = img_src_1.astype("float64")
        img_src_2 = img_src_2.astype("float64")

        mnSet1, skelImg1 = self.__getMnSet(img_src_1)
        mnSet2, skelImg2 = self.__getMnSet(img_src_2)

        lenDists = [len(mnSet1), len(mnSet2)]
        ratio = (min(lenDists) / max(lenDists)) * 100
        if ratio < 70:
            return 0

        mnMatcher = MnMatcher()
        score = mnMatcher.match(mnSet1, mnSet2)
        return score
