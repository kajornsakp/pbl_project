from segmentator.segmentation import segment_image
from enhancer import image_enhance
from PIL import Image
import numpy
import cv2

img = Image.open("asset/101_1.tif") #load image from file
# segmentedImg = segment_image(img,25,85) #best threshold and size so far
# segmentedImg = segment_image(img,20,55) #threshold lv 1
# segmentedImg2 = segment_image(segmentedImg,15,60) #threshold lv 2
segmentedImg = segment_image(img,30,100) #for dataset with gray background
segmentedImg.show()
enhanced_image = Image.fromarray(image_enhance(numpy.asarray(segmentedImg)))
enhanced_image.show()