from PIL import Image, ImageStat
from math import sqrt
import numpy


def calAverage(block):
    return numpy.average(numpy.asarray(block))


def segment_image(im,W,T):
    """returns segmented image as pillow image object

            :param im: pillow image object
            :param W: size of segmentation block
            :param T: Threshold for segmentation
            :type arg1: Image
            :type arg2: int
            :type arg3: int
            :returns: Pillow image object
            :rtype: Image

            """
    x,y = im.size
    img = im.copy()
    for i in range(0,x,W):
        for j in range(0,y,W):
            block = img.crop((i,j,min(i+W,x),min(j+W,y)))
            if (calAverage(block) < T):
                whiteBlock = numpy.full((W,W),1,numpy.uint8)*255
                imgWhite = Image.fromarray(whiteBlock)
                img.paste(imgWhite,(i,j))
    mask = numpy.asarray(img)[0:x][0,:y] < T

    return img, mask


def groupSegmented(img):
    segmentedImg = segment_image(img, 30, 100)  # threshold lv 1
    # segmentedImg2 = segment_image(segmentedImg, 25, 110)  # threshold lv 2
    # segmentedImg2 = segment_image(segmentedImg, 20, 120)  # threshold lv 2
    return segmentedImg


import numpy as np


def normalise(img, mean, std):
    normed = (img - np.mean(img)) / (np.std(img));
    return normed


def ridge_segment(im, blksze, thresh):
    rows, cols = im.shape;

    im = normalise(im, 0, 1);  # normalise to get zero mean and unit standard deviation

    new_rows = np.int(blksze * np.ceil((np.float(rows)) / (np.float(blksze))))
    new_cols = np.int(blksze * np.ceil((np.float(cols)) / (np.float(blksze))))

    padded_img = np.zeros((new_rows, new_cols));
    stddevim = np.zeros((new_rows, new_cols));

    padded_img[0:rows][:, 0:cols] = im;

    for i in range(0, new_rows, blksze):
        for j in range(0, new_cols, blksze):
            block = padded_img[i:i + blksze][:, j:j + blksze];

            stddevim[i:i + blksze][:, j:j + blksze] = np.std(block) * np.ones(block.shape)

    stddevim = stddevim[0:rows][:, 0:cols]

    mask = stddevim > thresh;

    mean_val = np.mean(im[mask]);

    std_val = np.std(im[mask]);

    normim = (im - mean_val) / (std_val);

    return normim, mask