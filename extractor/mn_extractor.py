import cv2
import math
from minutiae.minutiae import Minutiae
from minutiae.minutiae import MType
from minutiae.point2f import Point2f

class MnExtractor(object):
    @staticmethod
    def getNeighbours(x, y, image):
        #Return 8-neighbours of image point P1(x,y) in a clockwise order
        img = image
        x_1, y_1, x1, y1 = x - 1, y - 1, x + 1, y + 1
        return [ img[x_1][y_1], img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],  #P1,P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1]]  # P6,P7,P8

    @staticmethod
    def getCrossingNumber1(neighbours):
        n = neighbours + neighbours[0:1]
        return sum((n1, n2) == (255, 0) for n1, n2 in zip(n, n[1:]))  # (P1,P2), (P2,P3), ... , (P7,P8), (P8,P1)

    @staticmethod
    def getCrossingNumber2(neighbours):
        n = neighbours + neighbours[0:1]
        return 0.5 * sum(abs(n1//255-n2//255) for n1, n2 in zip(n, n[1:]))  # (P1,P2), (P2,P3), ... , (P7,P8), (P8,P1)

    @staticmethod
    def extract(skeletonedImg):
        mnSet = []
        # mnEndPoint = []
        # mnBifurc = []
        imgTemp = skeletonedImg.copy()
        rows, cols = imgTemp.shape
        margin = 15
        for x in range(margin, rows - margin):  # for each pixels (except the borders)
            for y in range(margin, cols - margin):
                if skeletonedImg[x, y] == 0:
                    P1, P2, P3, P4, P5, P6, P7, P8 = neighbours = MnExtractor.getNeighbours(x, y, skeletonedImg)  # get neighbours
                    P9 = P1

                    cn = MnExtractor.getCrossingNumber1(neighbours)
                    cn2 = MnExtractor.getCrossingNumber2(neighbours)

                    if(cn == 1 and cn2 == 1.0):
                        mnSet.append(Minutiae(Point2f(y,x), MType.ENDPOINT))
                    elif(cn >= 3 and cn2 >= 3.0):
                        mnSet.append(Minutiae(Point2f(y,x), MType.BIFURCATION))

        # for minutiae in mnSet:
        #     print(minutiae.getXY(), minutiae.getType())
        # finalEndPoint = []
        # finalBifurc = []
        # boolean = True
        # for bif in mnBifurc:
        #     bx,by = bif.getXY()
        #     boolean = True
        #     for endP in mnEndPoint:
        #         ex,ey = endP.getXY()
        #         dist = math.sqrt((ex-bx)*(ex-bx) + (ey-by)*(ey-by))
        #         if(dist > 20):
        #             print(bx,by,":",ex,ey,"=",dist)
        #             finalEndPoint.append(endP)
        #             if boolean:
        #                 finalEndPoint.append(bif)
        #                 boolean = False

        #mnSet = finalBifurc + finalEndPoint

        # imgToColor = cv2.cvtColor(imgTemp, cv2.COLOR_GRAY2BGR)
        # extractedImg = imgToColor
        # for minutiae in mnSet:
        #     if(minutiae.getType() == MType.ENDPOINT):
        #         extractedImg = cv2.circle(extractedImg, minutiae.getXY(), 3, (0, 0, 255), 2)
        #     elif(minutiae.getType() == MType.BIFURCATION):
        #         extractedImg = cv2.circle(extractedImg, minutiae.getXY(), 3, (255, 0, 0), 2)

        #extractedImg = cv2.circle(extractedImg, (192, 495), 3, (0, 0, 255), 2)

        # cv2.imshow("extracted", extractedImg)

        return mnSet