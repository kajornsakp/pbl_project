# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:50:30 2016

@author: utkarsh
"""
from .ridge_segment import ridge_segment
from .ridge_orient import ridge_orient
from .ridge_freq import ridge_freq
from .ridge_filter import ridge_filter
import cv2
import math
from PIL import Image, ImageDraw
import numpy as np


def image_enhance(img, mask):
    blksze = 16;
    thresh = 0.1;
    # normim,mask1 = ridge_segment(img,blksze,thresh);             # normalise the image and find a ROI

    #cv2.imshow('normin', normim)

    normim = img

    gradientsigma = 1;
    blocksigma = 7;
    orientsmoothsigma = 7;
    orientim = ridge_orient(img, gradientsigma, blocksigma, orientsmoothsigma);
    # find orientation of every pixel

    def get_line_ends(i, j, W, tang):
        if -1 <= tang and tang <= 1:
            begin = (i, (-W / 2) * tang + j + W / 2)
            end = (i + W, (W / 2) * tang + j + W / 2)
        else:
            begin = (i + W / 2 + W / (2 * tang), j + W / 2)
            end = (i + W / 2 - W / (2 * tang), j - W / 2)
        return (begin, end)

    im = Image.fromarray(img)
    (x, y) = im.size
    result = im.convert("RGB")
    angles = orientim
    draw = ImageDraw.Draw(result)

    for i in range(1, x, blocksigma):
        for j in range(1, y, blocksigma):
            tang = math.tan(angles[(i - 1) / blocksigma][(j - 1) / blocksigma])

            (begin, end) = get_line_ends(i, j, blocksigma, tang)
            draw.line([begin, end], fill=150)

    del draw
    cv2.imshow('ori', result)


    blksze = 38;
    windsze = 5;
    minWaveLength = 5;
    maxWaveLength = 15;
    freq, medfreq = ridge_freq(img, mask, orientim, blksze, windsze, minWaveLength,maxWaveLength);    #find the overall frequency of ridges

    freq = medfreq*mask;
    kx = 0.65;ky = 0.65;
    newim = ridge_filter(img, orientim, freq, kx, ky);       # create gabor filter and do the actual filtering


    #th, bin_im = cv2.threshold(np.uint8(newim),0,255,cv2.THRESH_BINARY);
    return newim