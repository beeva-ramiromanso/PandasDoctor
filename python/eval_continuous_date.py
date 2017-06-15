import pandas as pd
import numpy as np
import eval_datecol as dc
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


def eval_continuous_date(df,column_list,granularity='days',print_invalid=False):

    """
    Evaluates if the date columns are:
        1. In a valid date format
        2. Unique date values for each row
        3. Continuous with a given granularity.

    Test if the difference between the max and min date in a column matches the amount of elements with a given granularity.
    Doesn't require to be sorted.

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        column_list (list, str) -- A list of columns names to evaluate in the dataframe(df). A single
            column name can be detected and converted into a single element list
        granularity (str) -- Granularity of the dates. ['days','hours','minutes',
            'seconds','milliseconds']
        print_invalid (boolean) -- If true will print the rows of the dataframe
            where NA's have been found
    """
    # TODO - Add methods for mensual and anual granularity
    # TODO - Add print invalid funcionality
    if not isinstance(column_list,list): column_list = [column_list]
    found_bad_dates = False
    for col in column_list:
        if sum(df.duplicated(col,keep=False))>0:
            found_bad_dates = True
            print("Duplicated dates found!")
        elif not dc.eval_datecol(df,col):
            dates = df[col].apply(parse,dayfirst=True) #maybe df len ?
            tdelta = dates.max() - dates.min()
            result = delta_subtraction(tdelta,dates.shape[0],granularity) == 0
            if not result:
                print("Non continuous dates in column {0} for the given granularity {1}".format(col,granularity))
                found_bad_dates = True
    return(found_bad_dates)
