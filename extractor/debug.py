import cv2
from extractor.binarizer import Binarizer

if __name__ == '__main__':
    img = cv2.imread("../asset/101_1.tif", cv2.IMREAD_GRAYSCALE)
    binarizedImg = Binarizer.binarize(img)


    cv2.imshow("original", img)
    cv2.imshow("binarziedImg", binarizedImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

