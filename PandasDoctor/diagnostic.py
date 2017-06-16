import pandas as pd
import numpy as np
from evaluators import eval_NA,eval_outliers,eval_whitespaces,eval_continuous_date,eval_datecol


def diagnostic(df,print_invalid=False,continuous_dates = False):
    # TODO - Allow to evaluate the date columns by hand, not already validated ones
    """
    Runs a diagnostic for a Pandas Dataframe.

    Will determine the status of:
        * Existing NA and known NA' aliases (None, NULL...) in all the columns
        * Existing outliers in numeric columns using z_score or iqr
        * Existing leading or trailing whitespaces in categorical columns
        * Valid date formats in date columns
        * If selected, evaluate if date columns have continuous dates with a given granularity (default: days)

    Keyword arguments:
        df (pandas.DataFrame) -- The input DataFrame
        print_invalid (boolean) -- If true will print the rows of the dataframe
            where problems for each category have been found (currently only NA, Outliers, Whitespaces)
        continuous_dates (boolean) -- determine if date columns have continous dates
    """
    numeric_columns =  list(df.select_dtypes(include=[np.number]).columns.values)
    string_columns =  list(df.select_dtypes(include=['category']).columns.values)
    date_columns =  list(df.select_dtypes(include=['datetime']).columns.values)

    results = list()
    print("##########################")
    print("Validating NA")
    print("--------------------------")
    results = {"na_status":None,"numeric_status":None,"whitespace_status":None,
    "date_status":None}
    results["na_status"] = eval_NA(df,list(df.columns.values),print_invalid)

    #evaluating emptiness!
    print("##########################")
    print("Validating outliers")
    print("--------------------------")
    if numeric_columns:
        results["numeric_status"] = eval_outliers(df,numeric_columns,print_invalid=print_invalid)
    else:
        print("No numeric columns to validate, skiping...")

    print("##########################")
    print("Validating whitespaces")
    print("--------------------------")
    if string_columns:
        results["whitespace_status"] = eval_whitespaces(df,string_columns)
    else:
        print("No string columns to validate, skiping...")
    print("##########################")
    print("Validating Dates")
    print("--------------------------")
    if date_columns:
        date_status = False
        if continuous_dates:
            results["date_status"] = eval_continuous_date(df,date_columns)
        else:
            results["date_status"] = eval_datecol(df,date_columns)
    else:
        print("No date columns to validate, skiping...")
    print("##########################")
    return(results)
