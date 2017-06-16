import unittest
import pandas as pd
import numpy as np
from PandasDoctor import diagnostic

class TestDiagnostic(unittest.TestCase):

    def setUp(self):
        # x = pd.DataFrame({"col1":["A","B","C"],
        #                   "col2":["D","E","F"],
        #                   "col3":[1,2,3],
        #                   "col4":["D","E","F"],
        #                   "col5":["D","E","F"]
        #                   })
        # # Add three outliers...
        # y = pd.DataFrame({"col1":["NA","NULL","C"],
        #                   "col2":["D","-999","999"],
        #                   "col3":[999,-999,3],
        #                   "col4":["D",None,"F"],
        #                   "col5":["D","E","F"]
        #                   })
        # self.x = x.append(y,ignore_index=True)
        df1 = pd.DataFrame({ 'A' : [1.,2.,3.,4.],
                    'B' : pd.date_range('20130101',periods=4),
                    'C' : pd.Series([5,6,7,8],index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo' })
        #now another version with errors
        df2 = pd.DataFrame({ 'A' : [10.],
                    'B' : pd.to_datetime('20130110', format='%Y%m%d', errors='ignore'),
                    'C' : None,
                    'D' : 1.5,
                    'E' : pd.Categorical(["N/A"]),
                    'F' : 'foo ' })
        self.df1 = df1
        self.df2 = df1.append(df2)
        self.df2['E'] = df2['E'].astype('category')
        self.df2['F'] = df2['F'].astype('category')

    def test(self):
        x = diagnostic(self.df1)
        self.assertFalse(any(v for v in x.itervalues()))
        #self.assertFalse(x['na_status'])

        #    results = {"na_status":None,"numeric_status":None,"whitespace_status":None,
        #    "date_status":None}
        # self.assertTrue(evaluate_NA(self.x,['col1','col2','col3','col4']))
        # self.assertTrue(evaluate_NA(self.x,'col1'))
        # self.assertFalse(evaluate_NA(self.x,['col5']))

if __name__ == "__main__":
    unittest.main()
