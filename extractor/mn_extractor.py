import cv2
from minutiae.minutiae import Minutiae
from minutiae.minutiae import MType
from minutiae.point2f import Point2f

class MnExtractor(object):
    @staticmethod
    def getNeighbours(x, y, image):
        #Return 8-neighbours of image point P1(x,y) in a clockwise order
        img = image
        x_1, y_1, x1, y1 = x - 1, y - 1, x + 1, y + 1
        return [img[x_1][y_1], img[x_1][y], img[x_1][y1], img[x][y1], img[x1][y1],  #P1,P2,P3,P4,P5
                img[x1][y], img[x1][y_1], img[x][y_1]]  # P6,P7,P8

    @staticmethod
    def getCrossingNumber(neighbours):
        n = neighbours
        #return 0.5 * sum(abs(n1//255-n2//255) for n1, n2 in zip(n, n[1:]))  # (P1,P2), (P2,P3), ... , (P8,P1), (P1,P2)
        return 0.5 * sum(abs(n1//255-n2//255) for n1, n2 in zip(n, n[1:]))  # (P2,P3), (P3,P4), ... , (P8,P9), (P9,P2)

    @staticmethod
    def extract(skeletonedImg):
        mnSet = []
        imgTemp = skeletonedImg.copy()
        rows, cols = imgTemp.shape
        for x in range(1, rows - 1):  # for each pixels (except the borders)
            for y in range(1, cols - 1):
                P2, P3, P4, P5, P6, P7, P8, P9 = neighbours = MnExtractor.getNeighbours(x, y, skeletonedImg)  # get neighbours
                P1 = P9
                cn = MnExtractor.getCrossingNumber(neighbours)
                if(cn == 1.0):
                    mnSet.append(Minutiae(Point2f(y,x), MType.ENDPOINT))
                elif(cn == 3.0):
                    mnSet.append(Minutiae(Point2f(y,x), MType.BIFURCATION))

        for minutiae in mnSet:
            print(minutiae.getXY(), minutiae.getType())
        imgToColor = cv2.cvtColor(imgTemp, cv2.COLOR_GRAY2BGR)
        extractedImg = imgToColor
        for minutiae in mnSet:
            if(minutiae.getType() == MType.ENDPOINT):
                extractedImg = cv2.circle(extractedImg, minutiae.getXY(), 3, (0, 0, 255), 2)
            if(minutiae.getType() == MType.BIFURCATION):
                extractedImg = cv2.circle(extractedImg, minutiae.getXY(), 3, (0, 255, 255), 2)

        #extractedImg = cv2.circle(extractedImg, (192, 495), 3, (0, 0, 255), 2)

        cv2.imshow("extracted", extractedImg)

        return mnSet