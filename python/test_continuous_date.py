import pandas as pd
import numpy as np
import test_datecol as dc
from dateutil.parser import parse

_granularity = {'days':0,'hours':1,'minutes':2,'seconds':3,
'milliseconds':4,'microseconds':5,'nanoseconds':6}

def delta_subtraction(tdelta_input,nrows,granularity):
    return{
        'days':tdelta_input.components[_granularity[granularity]] - pd.Timedelta(days=nrows - 1).components[_granularity[granularity]],
        'hours':tdelta_input.components[_granularity[granularity]] - pd.Timedelta(hours=nrows - 1).components[_granularity[granularity]],
        'minutes':tdelta_input.components[_granularity[granularity]] - pd.Timedelta(minutes=nrows - 1).components[_granularity[granularity]],
        'seconds':tdelta_input.components[_granularity[granularity]] - pd.Timedelta(seconds=nrows - 1).components[_granularity[granularity]],
        'milliseconds':tdelta_input.components[_granularity[granularity]] - pd.Timedelta(milliseconds=nrows - 1).components[_granularity[granularity]]
    }[granularity]


def test_continuous_date(df,column_list,granularity='days'):
    """
    Test if the difference between the max and min date in a column matches the amount of elements with a given granularity.
    Doesn't require to be sorted.
    """
    if not isinstance(column_list,list): column_list = [column_list]
    all_correct = True
    for col in column_list:
        if sum(df.duplicated(col,keep=False))>0:
            print("Duplicated dates found!")
            all_correct = False
        elif dc.test_datecol(df,col):
            dates = df[col].apply(parse,dayfirst=True) #maybe df len ?
            tdelta = dates.max() - dates.min()
            result = delta_subtraction(tdelta,dates.shape[0],granularity) == 0
            if not result:
                print("Non continuous dates in column {0} for the given granularity {1}".format(col,granularity))
                all_correct = False
    return(all_correct)
