from segmentator.segmentation import segment_image
from enhancer import image_enhance
from PIL import Image
import numpy
import cv2

img = Image.open("asset/101_1.tif") #load image from file
# segmentedImg = segment_image(img,25,85) #best threshold and size so far
segmentedImg = segment_image(img,15,55) #threshold lv 1
segmentedImg2 = segment_image(segmentedImg,15,60) #threshold lv 2
enhanced_image = Image.fromarray(image_enhance(numpy.asarray(segmentedImg2)))
enhanced_image.show()