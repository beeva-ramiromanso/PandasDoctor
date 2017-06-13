import pandas as pd
import numpy as np

def z_score(arr,threshold = 3.5):
    """
     Returns a boolean array with True if points are outliers and False otherwise.

     Parameters:
     -----------
        points : An numobservations by numdimensions array of observations
        thresh : The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.

    Returns:
    --------
        mask : A numobservations-length boolean array.

     References: https://stackoverflow.com/questions/22354094/pythonic-way-of-detecting-outliers-in-one-dimensional-observation-data
    """

    std_modifier = 0.6745

    if len(arr.shape) == 1:
        arr = arr[:,None]
    median = np.median(arr, axis=0)
    diff = np.sum((arr - median)**2, axis=-1)
    diff = np.sqrt(diff)
    med_abs_deviation = np.median(diff)

    # The 0.6745 is to make the values roughly equivalent in units to standard deviations and
    # the 3.5 is the recommended threshold (roughly equivalent to 3.5 standard deviations).
    modified_z_score = std_modifier * diff / med_abs_deviation

    return modified_z_score > threshold

def detect_outliers(df, threshold = 3.5, plot = False):
    #identiy numeric columns
    ind = list(df.select_dtypes(include=[np.number]).columns.values)

    # default mode in R outliers package is z-scores => (x-mean)/sd

    res = list()
    found_outliers = False
    for col in ind:
        tmp = z_score(df[col])
        out = np.sum(tmp)
        if out > 0:
            res.append(tmp)
            found_outliers = True
            print("{0} Outliers found in var {1}".format(out,col))

    if not found_outliers:
        print("No outliers found in any var!")

    return(res)
