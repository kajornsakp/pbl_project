import cv2
import numpy as np;
import sys

from .image_enhance import image_enhance


if(len(sys.argv)<2):
    print('loading sample image')
    img_name = '1.jpg'
    img = cv2.imread('../images/' + img_name)
elif(len(sys.argv) >= 2):
    img_name = sys.argv[1];
    img = cv2.imread(sys.argv[1])
    
if(len(img.shape)>2):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
rows,cols = np.shape(img)
aspect_ratio = np.double(rows)/np.double(cols)

new_rows = 350             # randomly selected number
new_cols = int(new_rows//aspect_ratio)
print(new_rows, new_cols)
img = cv2.resize(img, (new_rows,new_cols))

enhanced_img = image_enhance(img)

# if(1):
#     print('saving the image')
#     c
#     cv2.imwrite('../enhanced/' + img_name,enhanced_img)
# else:
cv2.imshow('enhanced', enhanced_img)
cv2.waitKey()
