import numpy as np
import utils
import cv2
import scipy.ndimage as ndimage
from scipy import signal


def sobelKernelX():
    return np.array([[-1,  0,  1],
                     [-2,  0,  2],
                     [-1,  0,  1]])

def sobelKernelY():
    return np.array([[-1, -2, -1],
                     [ 0,  0,  0],
                     [ 1,  2,  1]])

def findOrientations(image, w=16, interpolate=True):
    """
    Estimate orientations of lines or ridges in an image.
    :param image: The image to estimate orientations in.
    :param w: The block size.
    :returns: An ndarray the same shape as the image, filled with orientation
              angles in radians.
    """

    height, width = image.shape

    # First we smooth the whole image with a Gaussian filter, to make the
    # individual pixel gradients less spurious.
    image = ndimage.filters.gaussian_filter(image, 2.0)

    # Compute the gradients G_x and G_y at each pixel
    G_x = utils.convolve(image, sobelKernelX())
    G_y = utils.convolve(image, sobelKernelY())

    # Estimate the local orientation of each block
    yblocks, xblocks = height // w, width // w
    O = np.empty((yblocks, xblocks))
    for j in range(yblocks):
        for i in range(xblocks):
            V_y, V_x = 0, 0
            for v in range(w):
                for u in range(w):
                    V_x += 2 * G_x[j*w+v, i*w+u] * G_y[j*w+v, i*w+u]
                    V_y += G_x[j*w+v, i*w+u] ** 2 - G_y[j*w+v, i*w+u] ** 2

            O[j, i] = np.arctan2(V_x, V_y) * 0.5

    # Rotate the orientations so that they point along the ridges, and wrap
    # them into only half of the circle (all should be less than 180 degrees).
    O = (O + np.pi * 0.5) % np.pi

    # Smooth the orientation field
    orientations = np.full(image.shape, -1.0)
    O_p = np.empty(O.shape)
    O = np.pad(O, 2, mode="edge")
    for y in range(yblocks):
        for x in range(xblocks):
            surrounding = O[y:y+5, x:x+5]
            orientation, deviation = utils.averageOrientation(surrounding, deviation=True)
            if deviation > 0.5:
                orientation = O[y+2, x+2]
            O_p[y, x] = orientation
    O = O_p

    # Make an orientation field the same shape as the input image, and fill it
    # with values interpolated from the preliminary orientation field.
    orientations = np.full(image.shape, -1.0)
    if interpolate:
        hw = w // 2
        for y in range(yblocks - 1):
            for x in range(xblocks - 1):
                for iy in range(w):
                    for ix in range(w):
                        orientations[y*w+hw+iy, x*w+hw+ix] = utils.averageOrientation(
                                [O[y, x], O[y+1, x], O[y, x+1], O[y+1, x+1]],
                                [iy + ix, w - iy + ix, iy + w - ix, w - iy + w - ix])
    else:
        for y in range(yblocks):
            for x in range(xblocks):
                orientations[y*w:(y+1)*w, x*w:(x+1)*w] = O[y, x]

    return orientations
