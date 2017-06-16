# PandasDoctor

### Example use:

```python

from PandasDoctor import diagnostic
import pandas as pd
import numpy as np

df1 = pd.DataFrame({ 'A' : [1.,2.,3.,4.],
                    'B' : pd.date_range('20130101',periods=4),
                    'C' : pd.Series([5,6,7,8],index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })

diagnostic(df1)

```

    ##########################
    Validating NA
    --------------------------
    No missing values found in any var!
    ##########################
    Validating outliers
    --------------------------
    [WARN] Values in column D seem to be constant, is this ok?
    No outliers found in any var!
    ##########################
    Validating whitespaces
    --------------------------
    No leading or trailing whitespaces found in any column!
    ##########################
    Validating Dates
    --------------------------
    No incorrect date formats found!
    ##########################
      
    {'date_status': Fals Bete,
    'na_status': False,
    'numeric_status': False,
    'whitespace_status': False}

### Better example with actual problems.

```python
df2 = pd.DataFrame({ 'A' : [10.],
                    'B' : pd.to_datetime('20130110', format='%Y%m%d', errors='ignore'),
                    'C' : None,
                    'D' : 1.5,
                    'E' : pd.Categorical(["N/A"]),
                    'F' : 'foo ' })
                    
df1 = df1.append(df2)
df1['E'] = df1['E'].astype('category')

diagnostic(df1,print_invalid=True,continuous_dates=True)

```

    ##########################
    Validating NA
    --------------------------
    [ERROR] NA values found in var C
    [ERROR] 1 NA Aliases found in var E
    ===================================
    Conflicting rows
    ===================================
          A          B     C    D    E     F
    0  10.0 2013-01-10  None  1.5  N/A  foo 
    ##########################
    Validating outliers
    --------------------------
    [ERROR] 1 Outliers found in var A
    [WARN] Median absolute deviation in the column D is 0 (corrected to 0.1), validate the column please
    [ERROR] 1 Outliers found in var D
    ===================================
    Conflicting rows
    ===================================
          A          B     C    D    E     F
    0  10.0 2013-01-10  None  1.5  N/A  foo 
    ##########################
    Validating whitespaces
    --------------------------
    No leading or trailing whitespaces found in any column!
    ##########################
    Validating Dates
    --------------------------
    No incorrect date formats found!
    [ERROR] Non continuous dates in column B for the given granularity days
    ##########################
    
    {'date_status': True,
    'na_status': True,
    'numeric_status': True,
    'whitespace_status': False}
 ```
