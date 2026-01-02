import numpy as np


def invert_binary(img_bin):
    """Invert a binary-like image array (0 <-> max)."""
    result = img_bin.max() - img_bin
    return result.astype(np.float32)


def blackout_pixels(img, img_bin):
    """Set pixels to 0 where img_bin is above its midpoint threshold."""
    result = img.copy()
    threshold = 0.5 if img_bin.max() <= 1 else img_bin.max() / 2
    result[img_bin > threshold] = 0
    return result.astype(np.float32)


def raise_nonblack_pixels(img, increment):
    """Increase non-zero pixels by increment, clipping to original max."""
    result = img.copy()
    result[result > 0] += increment
    result = np.clip(result, 0, img.max())
    return result.astype(np.float32)


def combine_regions(T1_0, T1_1, T1_2, T1_3, T1_4, T1_5):
    """Combine six binary region masks into a single labeled mask 0...5."""
    T1_0[T1_0 == 1] = 0
    T1_1[T1_1 == 1] = 1
    T1_2[T1_2 == 1] = 2
    T1_3[T1_3 == 1] = 3
    T1_4[T1_4 == 1] = 4
    T1_5[T1_5 == 1] = 5
    result = T1_0 + T1_1 + T1_2 + T1_3 + T1_4 + T1_5
    return result
