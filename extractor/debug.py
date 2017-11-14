import cv2
import numpy as np
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance
from segmentator.segmentation import segment_image
from PIL import Image

if __name__ == '__main__':
    #img = cv2.imread("../asset/102_1.tif", cv2.IMREAD_GRAYSCALE)

    img = Image.open("../asset/101_1.tif")  # load image from file
    originalImg = np.array(img)

    #Image Segmentation
    segmentedImgLvl1 = segment_image(img, 15, 55)  # threshold lv 1
    segmentedImg = np.asarray(segment_image(segmentedImgLvl1, 15, 60))  # threshold lv 2

    #Apply Gabor Filter
    enhancedImg = image_enhance(segmentedImg)

    #Binarize Image
    binarizedImg = Binarizer.binarize(enhancedImg)

    #Skeletonize Image
    skeletonedImg = Skeletonizer.skeletonize(binarizedImg)

    cv2.imshow("original", originalImg)
    cv2.imshow("segmentedImg", segmentedImg)
    cv2.imshow("enhanced Gabor", enhancedImg)
    cv2.imshow("binarziedImg", binarizedImg)
    cv2.imshow("skeletonizedImg", skeletonedImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

