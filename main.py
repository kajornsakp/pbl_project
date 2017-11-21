from datetime import datetime
import matcher.fp_matcher as FpMatcher
import scipy.ndimage as ndimage
import cv2

if __name__ == '__main__':
    startTime = datetime.now()

    fpMatcher = FpMatcher.FpMatcher()
    mainImg = '7'
    inputImg = '7'
    for i in range(1, 5):
        s = '' + str(i)
        img1 = cv2.imread('./asset/' + mainImg + '_1.BMP', cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread('./asset/' + inputImg + '_' + s +'.BMP', cv2.IMREAD_GRAYSCALE)

        score = fpMatcher.match(img1, img2)
        print(score)

    # score = fpMatcher.match('./asset/6_1.BMP',
    #                 './asset/6_2.BMP')
    # print(score)

    print(datetime.now() - startTime)