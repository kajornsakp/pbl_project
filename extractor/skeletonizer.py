import cv2
import numpy as np
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
    def skeletonize(binarizedImg):
        imgTemp = binarizedImg.copy()
        rows, cols = imgTemp.shape
        while True:
            countPixels = 0
            for x in range(1, rows-1):   #for each pixels (except the borders)
                for y in range(1, cols-1):
                    P2, P3, P4, P5, P6, P7, P8, P9 = neighbours = Skeletonizer.getNeighbours(x, y, imgTemp)  # get neighbours
                    countBlack = 0
                    for pixel in neighbours:
                        if(pixel == 0):
                            countBlack += 1
                    if((imgTemp[x,y] == 0) and #for each black pixels
                           (2 <= countBlack <= 6) and #The number of black pixel neighbors is [2, 6]
                           (Skeletonizer.transitions(neighbours) == 1) and #The number of transitions from white to black = 1
                           (P2 == 255 or P4 == 255 or P6 == 255) and #p2, p4, or p6 is white
                           (P4 == 255 or P6 == 255 or P8 == 255)): #p4, p6, or p8 is white
                        #print("In:",x,",",y)
                        imgTemp[x,y] = 255
                        countPixels += 1

            countPixels2 = 0
            for x in range(1, rows - 1):  # for each pixels (except the borders)
                for y in range(1, cols - 1):
                    P2, P3, P4, P5, P6, P7, P8, P9 = neighbours = Skeletonizer.getNeighbours(x, y, imgTemp)  # get neighbours
                    countBlack = 0
                    for pixel in neighbours:
                        if (pixel == 0):
                            countBlack += 1
                    if ((imgTemp[x, y] == 0) and  # for each black pixels
                            (2 <= countBlack <= 6) and  # The number of black pixel neighbors is [2, 6]
                            (Skeletonizer.transitions(neighbours) == 1) and  # The number of transitions from white to black = 1
                            (P2 == 255 or P4 == 255 or P8 == 255) and  # p2, p4, or p6 is white
                            (P2 == 255 or P6 == 255 or P8 == 255)):  # p4, p6, or p8 is white
                        #print("In2:", x, ",", y)
                        imgTemp[x, y] = 255
                        countPixels2 += 1

            if (countPixels2 == 0 and countPixels == 0):
                break

        skeletonedImg = imgTemp

        return skeletonedImg