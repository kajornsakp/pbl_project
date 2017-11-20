import cv2
import numpy as np
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance
from segmentator.segmentation import segment_image, ridge_segment
from extractor.mn_extractor import MnExtractor
from datetime import datetime

from PIL import Image

if __name__ == '__main__':
    img = cv2.imread("../asset/1_1.BMP", cv2.IMREAD_GRAYSCALE)

    # img = cv2.imread("../asset/skel-fp.png", cv2.IMREAD_GRAYSCALE)  # load image from file

    startTime = datetime.now()

    seg_img1, mask = segment_image(img, 60, 100)
    seg_img, mask = segment_image(seg_img1, 40, 60)
    enc_img = image_enhance(seg_img, mask)
    cv2.imshow("enc1", enc_img)
    cv2.imwrite('temp.png', enc_img)
    enc_img = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)
    bin_img = Binarizer.binarize(enc_img)
    ske_img = Skeletonizer.skeletonize(bin_img)
    mnSet = MnExtractor.extract(ske_img)

    print(datetime.now() - startTime)

    cv2.imshow("img", img)
    cv2.imshow("seg", seg_img)
    cv2.imshow("enc", enc_img)
    cv2.imshow("bin", bin_img)
    cv2.imshow("skel", ske_img)
    cv2.waitKey()
    cv2.destroyAllWindows()

