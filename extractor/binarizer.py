import cv2
import numpy as np

class Binarizer(object):

    @staticmethod
    def binarize(image):
        #convert float64 to uint8
        uint8Img = np.float32(image)
        #blur image
        #blurImg = cv2.GaussianBlur(uint8Img, (5, 5), 0)
        #binarize image
        retval, binarizedInvertImg = cv2.threshold(uint8Img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #invert color
        binarizedImg = cv2.bitwise_not(binarizedInvertImg)

        return binarizedImg