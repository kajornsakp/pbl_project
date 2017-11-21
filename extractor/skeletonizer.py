import cv2
import numpy as np

from skimage.morphology import skeletonize

class Skeletonizer(object):
    @staticmethod
    def skeletonize(img):
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
        blur = cv2.GaussianBlur(opening, (1, 1), 0)
        ret3, th4 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        th4[th4 == 255] = 1
        skel = skeletonize(th4)

        skel2 = np.ones(skel.shape, np.uint8)
        w, h = skel.shape
        for i in range(w):
            for j in range(h):
                if (skel[i][j]):
                    skel2[i][j] = 0
                else:
                    skel2[i][j] = 255

        return skel2