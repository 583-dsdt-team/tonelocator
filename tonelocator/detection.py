"""
Module defines the color detection function
"""

import cv2
import numpy as np
import os
import pandas as pd


rgb_df = pd.read_csv('./tonelocator/data/monk_scales_rgb.csv')
bw_df = pd.read_csv('./tonelocator/data/monk_scales_bw.csv')

def complexion_detection(image_path, rounding_places=2, grayscale=False):
    """
    Uses the inRange function in opencv
    Detects % of colors from ellis monk scale in image
    """
    filler = []
    path_check = os.path.isfile(image_path)

    if path_check is False:
        raise ValueError('File does not exist at this location')
    else:
        pass

    temp_image = cv2.imread(image_path)

    if temp_image is None:
        raise ValueError('Image file not read.')
    else:
        pass

    if grayscale is False:
        for index in range(rgb_df.shape[0]):
            upper = np.uint8([rgb_df['upper_b'][index], rgb_df['upper_g'][index], rgb_df['upper_r'][index]])
            lower = np.uint8([rgb_df['lower_b'][index], rgb_df['lower_g'][index], rgb_df['lower_r'][index]])
            mask = cv2.inRange(temp_image, lower, upper)
            cur_val = (mask > 0).mean()
            rounded_val = round(cur_val, rounding_places)
            filler.append(rounded_val)
    elif grayscale is True:
        for index in range(bw_df.shape[0]):
            upper = np.uint8([bw_df['upper_b'][index], bw_df['upper_g'][index], bw_df['upper_r'][index]])
            lower = np.uint8([bw_df['lower_b'][index], bw_df['lower_g'][index], bw_df['lower_r'][index]])
            mask = cv2.inRange(temp_image, lower, upper)
            cur_val = (mask > 0).mean()
            rounded_val = round(cur_val, rounding_places)
            filler.append(rounded_val)
    return(filler)
