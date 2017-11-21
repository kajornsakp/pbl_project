import numpy as np
import utils
import scipy.signal as signal

def findFrequencies(image, orientations, w=32):
    """
    Estimate ridge or line frequencies in an image, given an orientation field.

    This is more or less an implementation of of the algorithm in Chapter 2.5 in
    the paper:

        Fingerprint image enhancement: Algorithm and performance evaluation
        Hong, L., Wan, Y. & Jain, A. (1998)

    :param image: The image to estimate orientations in.
    :param orientations: An orientation field such as one returned from the
                         estimateOrientations() function.
    :param w: The block size.
    :returns: An ndarray the same shape as the image, filled with frequencies.
    """
    rotations = np.zeros(image.shape)

    height, width = image.shape
    yblocks, xblocks = height // w, width // w
    F = np.empty((yblocks, xblocks))
    for y in range(yblocks):
        for x in range(xblocks):
            orientation = orientations[y*w+w//2, x*w+w//2]

            block = image[y*w:(y+1)*w, x*w:(x+1)*w]
            block = utils.rotateAndCrop(block, np.pi * 0.5 + orientation)
            if block.size == 0:
                F[y, x] = -1
                continue

            utils.drawImage(block, rotations, y*w, x*w)

            columns = np.sum(block, (0,))
            columns = utils.normalize(columns)
            peaks = signal.find_peaks_cwt(columns, np.array([3]))
            if len(peaks) < 2:
                F[y, x] = -1
            else:
                f = (peaks[-1] - peaks[0]) / (len(peaks) - 1)
                if f < 5 or f > 15:
                    F[y, x] = -1
                else:
                    F[y, x] = 1 / f

    frequencies = np.full(image.shape, -1.0)
    F = np.pad(F, 1, mode="edge")
    for y in range(yblocks):
        for x in range(xblocks):
            surrounding = F[y:y+3, x:x+3]
            surrounding = surrounding[np.where(surrounding >= 0.0)]
            if surrounding.size == 0:
                frequencies[y*w:(y+1)*w, x*w:(x+1)*w] = -1
            else:
                frequencies[y*w:(y+1)*w, x*w:(x+1)*w] = np.median(surrounding)

    return frequencies


