from segmentator.segmentation import segment_image
from PIL import Image


img = Image.open("FPDB/1_1.BMP") #load image from file
# segmentedImg = segment_image(img,25,85) #best threshold and size so far
segmentedImg = segment_image(img,15,55) #threshold lv 1
segmentedImg2 = segment_image(segmentedImg,15,60) #threshold lv 2
segmentedImg2.show()