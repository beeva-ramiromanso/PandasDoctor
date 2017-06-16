import pandas as pd
import numpy as np
import json

_na_codes = ["missing", "no data", "na", "N/A", "n/a", "NULL", "NA"]
_na_numeric_codes = ["-999", "999", -999, 999]


def eval_NA(df,column_list,print_invalid=False):
    """
    Evaluates if NA exist in the selected columns of a dataframe

    Will check not only for NA, but for known aliases of NA.
    A list of missing value codes to check can be found in White et al. 2013.
    The list can be found in the na_codes.json file

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        column_list (list, str) -- A list of columns names to evaluate in the dataframe(df). A single
            column name can be detected and converted into a single element list
        print_invalid (boolean) -- If true will print the rows of the dataframe
            where NA's have been found
    """
    if not isinstance(column_list,list): column_list = [column_list]

    found_Missing = False
    na_list = np.full(df.shape[0], False, dtype=bool)
    for col in column_list:
        classic_na = df[col].isnull()
        if sum(classic_na)>0:
            found_Missing = True
            na_list = np.logical_or(na_list, classic_na)
            print("NA values found in var {0}".format(col))
        else:
            codes_tmp = df[col].isin(_na_codes)
            codes_out = np.sum(codes_tmp)
            numeric_tmp = df[col].isin(_na_numeric_codes)
            numeric_out = np.sum(numeric_tmp)
            if codes_out > 0:
                found_Missing = True
                na_list = np.logical_or(na_list, codes_tmp)
                print("{0} NA Aliases found in var {1}".format(codes_out,col))

            if numeric_out > 0:
                found_Missing = True
                na_list = np.logical_or(na_list, numeric_tmp)
                print("{0} 999-style aliases found in var {1}, that's usually a code for missing values, please verify!".format(numeric_out,col))

    if not found_Missing:
        print("No missing values found in any var!")
    elif print_invalid:
        print("###################################")
        print("Conflicting rows")
        print("###################################")
        print(df[na_list])
    return(found_Missing)
