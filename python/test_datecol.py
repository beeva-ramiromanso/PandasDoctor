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

def test_datecol(df,column_list,form='ymd'):
    if not isinstance(column_list,list): column_list = [column_list]
    allDatesCorrect = True
    for col in column_list:
        if not test_single_col(df[col]):
            print("Invalid date format found in column {0}".format(col))
            allDatesCorrect = False
    return(allDatesCorrect)
