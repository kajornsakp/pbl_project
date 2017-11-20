import cv2
import numpy as np


from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
from skimage.viewer import ImageViewer


class Skeletonizer(object):
    @staticmethod
    def getNeighbours(x, y, image):
        #Return 8-neighbours of image point P1(x,y) in a clockwise order
        img = image
        x_1, y_1, x1, y1 = x - 1, y - 1, x + 1, y + 1
        return [img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],  # P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1], img[x_1][y_1]]  # P6,P7,P8,P9

    @staticmethod
    def transitions(neighbours):
        #No. of 0,1 patterns (transitions from 0 to 1) in the ordered sequence
        n = neighbours + neighbours[0:1]  # P2, P3, ... , P8, P9, P2
        return sum((n1, n2) == (255, 0) for n1, n2 in zip(n, n[1:]))  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

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

    # @staticmethod
    # def skeletonize(binarizedImg):
    #
    #     imgTemp = binarizedImg.copy()
    #     rows, cols = imgTemp.shape
    #     while True:
    #         countPixels = 0
    #         for x in range(1, rows-1):   #for each pixels (except the borders)
    #             for y in range(1, cols-1):
    #                 if(imgTemp[x,y] == 0): #for each black pixels
    #                     P2, P3, P4, P5, P6, P7, P8, P9 = neighbours = Skeletonizer.getNeighbours(x, y, imgTemp)  # get neighbours
    #                     countBlack = 0
    #                     for pixel in neighbours:
    #                         if(pixel == 0):
    #                             countBlack += 1
    #                     if((2 <= countBlack <= 6) and #The number of black pixel neighbors is [2, 6]
    #                            (Skeletonizer.transitions(neighbours) == 1) and #The number of transitions from white to black = 1
    #                            (((P2 == 255 or P4 == 255 or P6 == 255) and #p2, p4, or p6 is white
    #                            (P4 == 255 or P6 == 255 or P8 == 255)) or
    #                                 ((P2 == 255 or P4 == 255 or P8 == 255) and  # p2, p4, or p6 is white
    #                             (P2 == 255 or P6 == 255 or P8 == 255)))): #p4, p6, or p8 is white
    #                         imgTemp[x,y] = 255
    #                         countPixels += 1
    #
    #         if (countPixels == 0):
    #             break
    #
    #     skeletonedImg = imgTemp
    #
    #     return skeletonedImg

    @staticmethod
    def skelPotae(img):
        # size = np.size(img)
        # skel = np.zeros(img.shape, np.uint8)
        #
        # ret, img = cv2.threshold(img, 127, 255, 0)
        # element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        # done = False
        #
        # while not done:
        #     eroded = cv2.erode(img, element)
        #     temp = cv2.dilate(eroded, element)
        #     temp = cv2.subtract(img, temp)
        #     skel = cv2.bitwise_or(skel, temp)
        #     img = eroded.copy()
        #
        #     zeros = size - cv2.countNonZero(img)
        #     if zeros == size:
        #         done = True
        #
        # return skel

        # img = img.copy()  # don't clobber original
        # skel = img.copy()
        # skel[:, :] = 0
        # kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
        #
        # while True:
        #     eroded = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)
        #     temp = cv2.morphologyEx(eroded, cv2.MORPH_DILATE, kernel)
        #     temp = cv2.subtract(img, temp)
        #     skel = cv2.bitwise_or(skel, temp)
        #     img[:, :] = eroded[:, :]
        #     if cv2.countNonZero(img) == 0:
        #         break
        #
        # return skel

        # img = invert(img)

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
        # viewer = ImageViewer(skel)
        # viewer.show()

        # fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
        #                          sharex=True, sharey=True,
        #                          subplot_kw={'adjustable': 'box-forced'})
        # ax = axes.ravel()
        #
        # ax[0].imshow(img, cmap=plt.cm.gray)
        # ax[0].axis('off')
        # ax[0].set_title('original', fontsize=20)
        #
        # ax[1].imshow(skel, cmap=plt.cm.gray)
        # ax[1].axis('off')
        # ax[1].set_title('skeleton', fontsize=20)
        #
        # fig.tight_layout()
        # plt.show()

        # skel = skeletonize(img)
        # print(type(skel))
        # cv2.imshow("skel", skel)
        return skel2
        # fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
        #                          sharex=True, sharey=True,
        #                          subplot_kw={'adjustable': 'box-forced'})
        # ax = axes.ravel()
        #
        # ax[0].imshow(img, cmap=plt.cm.gray)
        # ax[0].axis('off')
        # ax[0].set_title('original', fontsize=20)
        #
        # ax[1].imshow(skel, cmap=plt.cm.gray)
        # ax[1].axis('off')
        # ax[1].set_title('skeleton', fontsize=20)
        #
        # fig.tight_layout()
        # plt.show()