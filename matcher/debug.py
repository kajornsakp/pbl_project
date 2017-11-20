import math
import cv2
import numpy as np
from PIL import Image
from minutiae.minutiae import Minutiae, MType
from minutiae.point2f import Point2f
from matcher. mn_matcher import MnMatcher
import random as rand
from datetime import datetime
from extractor.binarizer import Binarizer
from extractor.skeletonizer import Skeletonizer
from enhancer.image_enhance import image_enhance
from segmentator.segmentation import segment_image
from extractor.mn_extractor import MnExtractor


def rotatePoint(centerPoint, point, angle):
    """Rotates a point around another centerPoint. Angle is in degrees.
    Rotation is counter-clockwise"""
    angle = math.radians(angle)
    r = (point[0] - centerPoint[0],
         point[1] - centerPoint[1])
    r = (r[0] * math.cos(angle) - r[1] * math.sin(angle),
         r[0] * math.sin(angle) + r[1] * math.cos(angle))
    r = (r[0] + centerPoint[0],
         r[1] + centerPoint[1])
    return r

if __name__ == '__main__':
    startTime = datetime.now()

    s1 = [
        (55, 13),
        (159, 14),
        (121, 15),
        (80, 19),
        (238, 19),
        (90, 22),
        (232, 25),
        (238, 25),
        (90, 26),
        (68, 30),
        (239, 30),
        (138, 32),
        (160, 40),
        (62, 42),
        (55, 44),
        (68, 45),
        (258, 45),
        (69, 51),
        (147, 53),
        (207, 54),
        (267, 63),
        (39, 70),
        (39, 71),
        (165, 71),
        (268, 73),
        (42, 74),
        (50, 75),
        (42, 76),
        (90, 81),
        (268, 86),
        (48, 90),
        (44, 91),
        (44, 93),
        (25, 96),
        (268, 97),
        (38, 99),
        (47, 99),
        (53, 99),
        (127, 103),
        (37, 106),
        (131, 108),
        (268, 109),
        (38, 120),
        (268, 125),
        (74, 131),
        (227, 131),
        (237, 131),
        (46, 133),
        (268, 136),
        (36, 149),
        (268, 150),
        (41, 154),
        (193, 154),
        (268, 160),
        (43, 165),
        (268, 171),
        (96, 175),
        (103, 175),
        (113, 176),
        (194, 176),
        (41, 178),
        (145, 181),
        (38, 183),
        (268, 183),
        (88, 185),
        (90, 185),
        (95, 186),
        (112, 187),
        (37, 188),
        (169, 188),
        (174, 188),
        (25, 192),
        (107, 192),
        (253, 192),
        (44, 194),
        (262, 194),
        (92, 197),
        (98, 197),
        (172, 199),
        (164, 200),
        (258, 203),
        (46, 204),
        (190, 211),
        (91, 213),
        (196, 214),
        (92, 215),
        (144, 215),
        (90, 216),
        (46, 218),
        (258, 218),
        (112, 220),
        (82, 221),
        (132, 221),
        (138, 222),
        (132, 223),
        (138, 223),
        (49, 224),
        (166, 224),
        (257, 230),
        (51, 234),
        (175, 236),
        (180, 237),
        (31, 238),
        (148, 238),
        (252, 238),
        (48, 239),
        (74, 241),
        (154, 245),
        (55, 246),
        (153, 246),
        (160, 246),
        (247, 246),
        (155, 247),
        (239, 250),
        (167, 251),
        (142, 252),
        (165, 252),
        (63, 253),
        (229, 255),
        (222, 256),
        (238, 256),
        (159, 257),
        (236, 261),
        (236, 262),
        (71, 263),
        (139, 266),
        (67, 267),
        (159, 267),
        (67, 268),
        (156, 268),
        (231, 269),
        (232, 269),
        (145, 270),
        (73, 271),
        (184, 271),
        (205, 271),
        (225, 271),
        (227, 271),
        (237, 271),
        (156, 273),
        (217, 275),
        (152, 276),
        (200, 277),
        (82, 278),
        (89, 281),
        (99, 281),
        (106, 281),
        (117, 282),
        (138, 282),
        (171, 282),
        (194, 282),
        (184, 283),
        (147, 284),
        (164, 285),
        (55, 287),
        (60, 287),
    ]
    s2 = [
        (170, 15),
        (189, 24),
        (195, 24),
        (219, 36),
        (228, 39),
        (101, 47),
        (232, 49),
        (117, 54),
        (53, 56),
        (171, 58),
        (236, 62),
        (113, 72),
        (239, 72),
        (29, 80),
        (33, 81),
        (137, 83),
        (243, 85),
        (38, 93),
        (31, 94),
        (39, 97),
        (28, 98),
        (246, 98),
        (250, 110),
        (69, 113),
        (16, 116),
        (17, 117),
        (252, 120),
        (228, 121),
        (214, 122),
        (108, 125),
        (116, 125),
        (26, 131),
        (28, 131),
        (256, 132),
        (29, 139),
        (21, 142),
        (24, 142),
        (34, 143),
        (260, 143),
        (20, 145),
        (30, 149),
        (259, 151),
        (186, 154),
        (69, 156),
        (25, 158),
        (25, 159),
        (250, 167),
        (265, 176),
        (195, 178),
        (31, 179),
        (99, 183),
        (265, 186),
        (38, 191),
        (95, 192),
        (150, 195),
        (268, 199),
        (38, 203),
        (115, 203),
        (99, 210),
        (105, 210),
        (115, 211),
        (199, 211),
        (132, 212),
        (118, 215),
        (207, 215),
        (130, 216),
        (46, 217),
        (106, 219),
        (111, 220),
        (105, 221),
        (46, 222),
        (268, 223),
        (44, 224),
        (156, 232),
        (181, 232),
        (191, 234),
        (107, 235),
        (157, 235),
        (259, 235),
        (49, 240),
        (286, 240),
        (168, 241),
        (259, 241),
        (191, 243),
        (153, 244),
        (259, 244),
        (271, 244),
        (268, 245),
        (98, 246),
        (102, 247),
        (126, 248),
        (259, 250),
        (96, 251),
        (102, 252),
        (251, 253),
        (53, 254),
        (244, 255),
        (95, 257),
        (99, 258),
        (185, 258),
        (98, 263),
        (208, 264),
        (94, 270),
        (185, 270),
        (57, 271),
        (72, 271),
        (165, 271),
        (91, 279),
        (164, 280),
        (85, 281),
        (164, 283),
        (172, 284),
        (183, 285),
        (98, 295),
        (99, 297),
    ]


    mnSet1 = []
    for mn in s1:
        mnSet1.append(Minutiae(Point2f(mn[0], mn[1])))

    mnSet2 = []
    keyPoint2 = []
    original_img = cv2.imread("skel-fp-2.jpg", cv2.IMREAD_GRAYSCALE)
    original_img = Binarizer.binarize(original_img)
    original_img = Skeletonizer.skeletonize(original_img)
    mnSet2 = MnExtractor.extract(original_img)

    # cv2.imshow("d", original_img)
    # cv2.waitKey()

    # for mn in s2:
    #     mnSet2.append(Minutiae(Point2f(mn[0], mn[1])))

    mnMatcher = MnMatcher()
    mnMatcher.match(mnSet1, mnSet2)
    print((datetime.now() - startTime))



'''
if __name__ == '__main__':

    # original_img = cv2.imread("original.png", cv2.IMREAD_GRAYSCALE)  # load image from file
    #
    # input_img = cv2.imread("input-2.png", cv2.IMREAD_GRAYSCALE)  # load image from file
    #
    # startTime = datetime.now()
    #
    # input_img = Binarizer.binarize(input_img)
    # input_img = Skeletonizer.skeletonize(input_img)
    #
    #
    # skel_fp_input = cv2.imread("../asset/skel-fp-input.png", cv2.IMREAD_GRAYSCALE)  # load image from file
    #
    #
    # mnSet1 = MnExtractor.extract(original_img)
    # mnSet2 = MnExtractor.extract(input_img)
    # print((datetime.now() - startTime).total_seconds())
 

    # cv2.imshow("skel_Img", input_img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

        # startTime = datetime.now()
    #
    # # start random points
    # w, h = 600, 600
    # n = 400
    #
    # mnSet1 = []
    # mTypes = [MType.ENDPOINT, MType.BIFURCATION]
    # for i in range(n):
    #     x = rand.randint(100, w - 100)
    #     y = rand.randint(100, h - 100)
    #
    #     posVal = Point2f(x, y)
    #     mType = mTypes[rand.randint(0, 1)]
    #
    #     mnSet1.append(Minutiae(posVal, mType))
    #
    # mnSet2 = []
    # centerPoint = (w/2, h/2)
    # for i in range(n):
    #     # point = (mnSet1[i].pos.x, mnSet1[i].pos.y)
    #     # x, y = rotatePoint(centerPoint, point, 30)
    #     #
    #     # posVal = Point2f(int(x), int(y))
    #     # mType = mTypes[rand.randint(0, 1)]
    #
    #     x = rand.randint(100, w - 100)
    #     y = rand.randint(100, h - 100)
    #
    #     posVal = Point2f(x, y)
    #     mType = mTypes[rand.randint(0, 1)]
    #
    #     mnSet2.append(Minutiae(posVal, mType))
    #
    # # img1 = np.zeros((w, h), np.uint8)
    # # for mn in mnSet1:
    # #     img1[mn.pos.x, mn.pos.y] = 255
    # #
    # # img2 = np.zeros((w, h), np.uint8)
    # # for mn in mnSet2:
    # #     img2[mn.pos.x, mn.pos.y] = 255
    #
    # mnMatcher = MnMatcher()
    # mnMatcher.match(mnSet1, mnSet2)
    #
    # print(datetime.now()-startTime)
    #
    # #
    # # cv2.imshow('original', img1)
    # # cv2.imshow('rotated', img2)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    '''