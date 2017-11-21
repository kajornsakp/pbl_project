import numpy as np

def binarize(image, w=32):
    """
    Perform a local binarization of an image. For each cell of the given size
    w, the average value is calculated. Every pixel that is below this value,
    is set to 0, every pixel above, is set to 1.

    :param image: The image to be binarized.
    :param w:     The size of the cell.
    :returns:     The binarized image.
    """

    image = np.copy(image)
    height, width = image.shape
    for y in range(0, height, w):
        for x in range(0, width, w):
            block = image[y:y+w, x:x+w]
            threshold = np.average(block)
            image[y:y+w, x:x+w] = np.where(block >= threshold, 1.0, 0.0)

    return image