import numpy as np
import utils
import enhancer.frequency as freq
import enhancer.orientation as orien
import enhancer.gabor as gabor

def enhancer(img, mask):
    img = np.where(mask == 1.0, utils.localNormalize(img), img)

    # Estimating orientations
    orientations = np.where(mask == 1.0, orien.findOrientations(img), -1.0)
    # utils.showOrientations(image, orientations, "orientations", 8)

    # Estimating frequencies
    frequencies = np.where(mask == 1.0, freq.findFrequencies(img, orientations), -1.0)

    # Filtering
    img = gabor.gaborFilter(img, orientations, frequencies)
    
    return img