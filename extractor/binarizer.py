import cv2
import numpy as np

class Binarizer(object):

    @staticmethod
    def binarize(image):
        uint8Img = image.astype(np.uint8)
        retval, binarizedInvertImg = cv2.threshold(uint8Img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        binarizedImg = cv2.bitwise_not(binarizedInvertImg)

        return binarizedImg