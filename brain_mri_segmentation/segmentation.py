import numpy as np
import cv2
from skimage.filters import threshold_multiotsu
from skimage.morphology import closing, area_closing
from skimage.segmentation import (
    morphological_chan_vese,
    morphological_geodesic_active_contour,
)


def multi_otsu_thresholding(img, classes):
    """Segment image into given classes using Multi-Otsu Thresholding."""
    thresholds = threshold_multiotsu(img, classes=classes)
    result = np.digitize(img, bins=thresholds)
    return result.astype(np.float32)

def chan_vese(img, n_iter=300, smoothing=1, iter_callback=lambda u: None):
    """Morphological Chan–Vese segmentation (MCV)."""
    result = morphological_chan_vese(img, num_iter=n_iter, init_level_set='disk',
                                   smoothing=smoothing, iter_callback=iter_callback)
    return result.astype(np.float32)

def geod_active_contour(img, n_iter=300, smoothing=1, balloon=1, threshold='auto', iter_callback=lambda u: None):
    """Morphological Geodesic Active Contour segmentation (MGAC)."""
    result = morphological_geodesic_active_contour(
        img, num_iter=n_iter, init_level_set='disk', smoothing=smoothing,
        balloon=balloon, threshold=threshold, iter_callback=iter_callback,
    )
    return result.astype(np.float32)

def area_close(img_bin, area_threshold):
    """Remove small holes in a binary volume by morphological area closing."""
    result = area_closing(img_bin > 0, area_threshold=area_threshold)
    return result.astype(np.float32)

def close(img):
    """Apply morphological closing to an image/volume."""
    result = closing(img)
    return result.astype(np.float32)

def kmeans_segmentation(img, k):
    """Segment image into k clusters using K-means, with labels ranked by intensity."""
    pixel_values = img.reshape(-1, 1).astype(np.float32)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, labels, centers = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    segmented = labels.reshape(img.shape)
    # Rank clusters by increasing center intensity.
    sorted_i = np.argsort(centers.ravel())
    rank_map = np.zeros_like(sorted_i)
    for rank, i in enumerate(sorted_i):
        rank_map[i] = rank
    # Remap segmentation labels to 0, 1, 2, ... etc.
    result = rank_map[segmented]
    return result.astype(np.float32)
