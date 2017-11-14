import cv2
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance


if __name__ == '__main__':
    img = cv2.imread("../asset/102_1.tif", cv2.IMREAD_GRAYSCALE)
    enhancedImg = image_enhance(img)
    binarizedImg = Binarizer.binarize(img)
    skeletonedImg = Skeletonizer.skeletonize(binarizedImg)

    cv2.imshow("original", img)
    cv2.imshow("enhanced", enhancedImg)
    cv2.imshow("binarziedImg", binarizedImg)
    cv2.imshow("skeletonizedImg", skeletonedImg)
    cv2.waitKey()
    cv2.destroyAllWindows()

