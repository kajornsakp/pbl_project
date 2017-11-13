import cv2


class Binarizer(object):

    @staticmethod
    def binarize(fpImg):
        retval, binarizedImg = cv2.threshold(fpImg, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        return binarizedImg