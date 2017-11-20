import cv2
import numpy as np
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance
from segmentator.segmentation import segment_image
from extractor.mn_extractor import MnExtractor
from datetime import datetime

from PIL import Image

if __name__ == '__main__':
    img = cv2.imread("../asset/102_1.tif", cv2.IMREAD_GRAYSCALE)

    img = cv2.imread("../asset/skel-fp.png", cv2.IMREAD_GRAYSCALE)  # load image from file

    startTime = datetime.now()

    bin_img = Binarizer.binarize(img)
    ske_img = Skeletonizer.skeletonize(bin_img)
    mnSet = MnExtractor.extract(ske_img)

    print(datetime.now() - startTime)

    cv2.imshow("skel", ske_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

