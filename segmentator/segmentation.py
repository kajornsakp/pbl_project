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
    return img


