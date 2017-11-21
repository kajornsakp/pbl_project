import numpy as np
import utils

def gaborKernel(size, angle, frequency):
    """
    Create a Gabor kernel given a size, angle and frequency.

    Code is taken from https://github.com/rtshadow/biometrics.git
    """

    angle += np.pi * 0.5
    cos = np.cos(angle)
    sin = -np.sin(angle)

    yangle = lambda x, y: x * cos + y * sin
    xangle = lambda x, y: -x * sin + y * cos

    xsigma = ysigma = 4

    return utils.kernelFromFunction(size, lambda x, y:
            np.exp(-(
                (xangle(x, y) ** 2) / (xsigma ** 2) +
                (yangle(x, y) ** 2) / (ysigma ** 2)) / 2) *
            np.cos(2 * np.pi * frequency * xangle(x, y)))

def gaborFilter(image, orientations, frequencies, w=32):
    result = np.empty(image.shape)

    height, width = image.shape
    for y in range(0, height - w, w):
        for x in range(0, width - w, w):
            orientation = orientations[y+w//2, x+w//2]
            frequency = utils.averageFrequency(frequencies[y:y+w, x:x+w])

            if frequency < 0.0:
                result[y:y+w, x:x+w] = image[y:y+w, x:x+w]
                continue

            kernel = gaborKernel(16, orientation, frequency)
            result[y:y+w, x:x+w] = utils.convolve(image, kernel, (y, x), (w, w))

    return utils.normalize(result)


