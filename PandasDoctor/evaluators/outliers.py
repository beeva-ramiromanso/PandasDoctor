import pandas as pd
import numpy as np

_methods = ['z_score','iqr']

def iqr(arr,range = 1.5,colname=None):
    """
     Returns a boolean array with True if points are outliers and False otherwise.

     Parameters:
     -----------
        arr -- Array of points
        range -- Size of the IQR to determine the margins of valid values. Anything above or below
            IQR * range will be marked as outlier.
        colname -- Name of the column to evaluate in case of error

    Returns:
    --------
        mask : A numobservations-length boolean array.

        References: http://stamfordresearch.com/outlier-removal-in-python-using-iqr-rule/
    """
    q75, q25 = np.percentile(arr, [75 ,25])
    iqr = q75 - q25
    min = q25 - (iqr*range)
    max = q75 + (iqr*range)
    return np.logical_or(arr<min, max<arr)


def z_score(arr,threshold = 3.5,colname=None):
    """
     Returns a boolean array with True if points are outliers and False otherwise.

     Parameters:
     -----------
        arr -- Array of points
        threshold -- The modified z-score to use as a threshold. Observations with
            a modified z-score (based on the median absolute deviation) greater
            than this value will be classified as outliers.
        colname -- Name of the column to evaluate in case of error, like absolute
            median deviation == 0

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
    if(med_abs_deviation == 0):
        print("[WARN] Median absolute deviation in the column {0} is 0 (corrected to 0.1), validate the column please".format(colname))

    # The 0.6745 is to make the values roughly equivalent in units to standard deviations and
    # the 3.5 is the recommended threshold (roughly equivalent to 3.5 standard deviations).
    modified_z_score = std_modifier * diff / (med_abs_deviation+0.1)

    return modified_z_score > threshold

def outlier_method(arr, method_parameter, method,colname):
    return{
        'z_score':z_score(arr,method_parameter,colname),
        'iqr':iqr(arr,method_parameter,colname)
    }[method]

def eval_outliers(df, column_list,
    method_parameter = 3.5, method='z_score',print_invalid=False):

    """
    Evaluates if outliers exists in the selected columns of a dataframe

    Uses z_score or iqr for outlier detection, default z_score

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        column_list (list, str) -- A list of columns names to evaluate in the dataframe(df). A single
            column name can be detected and converted into a single element list
        method_parameter (numeric) -- Value to use as parameter for the outlier detection
            method. Threshold for the z_score, range for the IQR.
        method (str) -- ['z_score','iqr'] Which method the funcion will use to determine outliers
        print_invalid (boolean) -- If true will print the rows of the dataframe
            where outliers have been found
    """
    #identiy numeric columns
    #ind = list(df.select_dtypes(include=[np.number]).columns.values)

    # TODO - validation needed for some params
    # TODO - So...division by zero man, by ZERO
    if not isinstance(column_list,list): column_list = [column_list]
    outlier_list = np.full(df.shape[0], False, dtype=bool)
    found_outliers = False
    for col in column_list:
        if(df[col].nunique() == 1):
            print("[WARN] Values in column {1} seem to be constant, is this ok?".format(nout,col))
        else:
            outliers_found = outlier_method(df[col], method_parameter, method,colname=col)
            nout = np.sum(outliers_found)
            if nout > 0:
                outlier_list = np.logical_or(outlier_list, outliers_found)
                found_outliers = True
                print("[ERROR] {0} Outliers found in var {1}".format(nout,col))

    if not found_outliers:
        print("No outliers found in any var!")
    elif print_invalid:
        print("===================================")
        print("Conflicting rows")
        print("===================================")
        print(df[outlier_list])
    return(found_outliers)
