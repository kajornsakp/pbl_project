import cv2
import numpy as np
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance
from segmentator.segmentation import segment_image
from extractor.mn_extractor import MnExtractor

from PIL import Image

if __name__ == '__main__':
    img = cv2.imread("../asset/101_1.tif", cv2.IMREAD_GRAYSCALE) # load image from file

    #Image Segmentation
    segmentedImg, mask = segment_image(img, 60, 100)  # threshold lv 1
    # segmentedImg2, mask = segment_image(segmentedImg, 15, 60)  # threshold lv 2

    #Apply Gabor Filter
    enhancedImg = image_enhance(segmentedImg, mask)

    #Binarize Image
    binarizedImg = Binarizer.binarize(enhancedImg)

    #Skeletonize Image
    skeletonedImg = Skeletonizer.skeletonize(binarizedImg)

    #Extract Minutiae
    mnSet = MnExtractor.extract(skeletonedImg)

    cv2.imshow("original", img)
    cv2.imshow("segmentedImg", segmentedImg)
    cv2.imshow("enhanced Gabor", enhancedImg)
    print(enhancedImg.dtype)
    cv2.imshow("binarziedImg", binarizedImg)
    cv2.imshow("skeletonizedImg", skeletonedImg)

    #skeletonedImg = cv2.imread("/Users/TUEY/Documents/KMITL SE 2016/Year 4 Term 1/CV/Assignment/pbl_project/asset/skeletonizedfingerprint.png", cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread("../asset/skeletonizedfingerprint.png", cv2.IMREAD_GRAYSCALE)
    #
    # binarizedImg = Binarizer.binarize(img)
    # skeletonedImg = Skeletonizer.skeletonize(binarizedImg)
    # mnSet = MnExtractor.extract(skeletonedImg)
    #
    # cv2.imshow("skeletonizedImg", skeletonedImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

