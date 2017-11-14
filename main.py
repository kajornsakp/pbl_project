from segmentator.segmentation import segment_image
from PIL import Image


img = Image.open("Image path") #load image from file
segmentedImg = segment_image(img,25,85) #best threshold and size so far
segmentedImg.show()
