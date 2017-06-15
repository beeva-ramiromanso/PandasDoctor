import pandas as pd
import numpy as np

def eval_whitespaces(df,column_list,print_invalid=False):
    """
    Evaluates if leading or trailing whitespaces exist in the selected columns of a dataframe

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        column_list (list, str) -- A list of columns names to evaluate in the dataframe(df). A single
            column name can be detected and converted into a single element list
        print_invalid (boolean) -- If true will print the rows of the dataframe
            where whitespaces have been found
    """
    if not isinstance(column_list,list): column_list = [column_list]
    found_whitespaces = False
    whitespace_list = np.full(df.shape[0], False, dtype=bool)
    for col in column_list:
        invalid_list = df[col].str.strip() != df[col]
        if sum(invalid_list)>0:
            found_whitespaces = True
            whitespace_list = np.logical_or(whitespace_list, invalid_list)
    if print_invalid:
        print(df[whitespace_list])
    return(found_whitespaces)
