import numpy as np
import utils

def findMask(image, threshold=0.1, w=32):
    """
    Create a mask image consisting of only 0's and 1's. The areas containing
    1's represent the areas that look interesting to us, meaning that they
    contain a good variety of color values.
    """
    image = utils.normalize(image)
    mask = np.empty(image.shape)
    height, width = image.shape
    for y in range(0, height, w):
        for x in range(0, width, w):
            block = image[y:y+w, x:x+w]
            standardDeviation = np.std(block)
            if standardDeviation < threshold:
                mask[y:y+w, x:x+w] = 0.0
            elif block.shape != (w, w):
                mask[y:y+w, x:x+w] = 0.0
            else:
                mask[y:y+w, x:x+w] = 1.0

    return image, mask
