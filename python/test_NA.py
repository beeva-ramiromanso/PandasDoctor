import pandas as pd
import numpy as np
import json

def test_for_NA(df):
    with open('na_codes.json') as data_file:
        codes = json.load(data_file)
        na_codes = codes["na_codes"]
        na_numeric_codes = codes["na_numeric_codes"]

    print("Loaded na codes: {}".format(na_codes))
    print("Loaded na numeric codes: {}".format(na_numeric_codes))

    res = list()
    found_outliers = False
    for col in df.columns:
        codes_tmp = df[col].isin(na_codes)
        codes_out = np.sum(codes_tmp)
        numeric_tmp = df[col].isin(na_numeric_codes)
        numeric_out = np.sum(numeric_tmp)
        if codes_out > 0:
            res.append(codes_tmp)
            found_outliers = True
            print("{0} Missing values found in var {1}".format(codes_out,col))

        if numeric_out > 0:
            res.append(numeric_tmp)
            print("{0} 999-style values found in var {1}, that's usually a code for missing values, please verify!".format(numeric_out,col))

    if not found_outliers:
        print("No missing values found in any var!")
    return(res)
