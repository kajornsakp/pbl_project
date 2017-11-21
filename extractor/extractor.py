import extractor.binarize as binarize
from extractor.skeletonizer import Skeletonizer
from extractor.mn_extractor import MnExtractor
import cv2
import numpy as np
import scipy.misc as misc

def extractor(img, mask):
    img = np.where(mask == 1.0, binarize.binarize(img), 1.0)
    misc.imsave('temp.png', img)
    img = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)

    # Skeletonizer
    ske_img = Skeletonizer.skeletonize(img)

    return MnExtractor.extract(ske_img)