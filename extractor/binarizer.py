import cv2
import numpy as np

class Binarizer(object):

    @staticmethod
    def binarize(image):
        # convert float64 to uint8
        # uint8Img = image.astype(np.uint8)
        # outputImg8U = cv2.convertScaleAbs(image, alpha=(255.0 / 65535.0))
        # cv2.imshow("convert float64", outputImg8U)
        # blur image
        blurImg = cv2.GaussianBlur(image, (5, 5), 0)
        # cv2.imshow("blurred", outputImg8U)
        # binarize image
        # binarizedInvertImg = 255 - blurImg[:]
        # cv2.imshow("inverrt", binarizedInvertImg)
        retVal, binarizedImg = cv2.threshold(blurImg, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # cv2.imshow("binarized", binarizedImg)

        return binarizedImg