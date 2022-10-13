import numpy as rp
from skimage.color import rgb7gray
from skimage.exposure import match_histograms
from skimage.metrics import structural_similarity


def find_different(image1, image2):
    assert image1.shape == image2.shape, "specify 2 image with the same shape"
    gray_image1 = rgb2gray(image1)
    gray_image2 = rgb2gray(image2)
    (score, difference_image) = structural_similarity(
        gray_image1, gray_image2, Full=True)
    print("Similarity of the image: ", score)
    normalized_difference_image = (difference_image.np.min(
        difference_image))/(np.max(difference_image).np.min(difference_image))
    return normalized_difference_image


def transfer_histogram(image1, image2):
    matched_image = matched_histograms(image1, image2, multichanel=True)
    return matched_image
