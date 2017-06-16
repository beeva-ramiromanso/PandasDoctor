import pandas as pd
import numpy as np
from dateutil.parser import parse

def test_single_col(arr):
    correctDate = True
    try:
        date = arr.apply(parse,dayfirst=True)
    except ValueError:
        correctDate = False
    return(correctDate)

def eval_datecol(df,column_list,form='ymd'):
    """
    Evaluates if leading or trailing whitespaces exist in the selected columns of a dataframe

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        column_list (list, str) -- A list of columns names to evaluate in the dataframe(df). A single
            column name can be detected and converted into a single element list
    """

    # TODO - Add print invalid funcionality here
    if not isinstance(column_list,list): column_list = [column_list]
    found_bad_dates = False
    for col in column_list:
        if not test_single_col(df[col]):
            found_bad_dates = True
            print("Invalid date format found in column {0}".format(col))
    return(found_bad_dates)
