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
        dates = pd.date_range('20130101',periods=6)
        self.x = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))

    def test(self):
        x = diagnostic(self.x,print_invalid=True)
        self.assertFalse(x['na_status'])

        #    results = {"na_status":None,"numeric_status":None,"whitespace_status":None,
        #    "date_status":None}
        # self.assertTrue(evaluate_NA(self.x,['col1','col2','col3','col4']))
        # self.assertTrue(evaluate_NA(self.x,'col1'))
        # self.assertFalse(evaluate_NA(self.x,['col5']))

if __name__ == "__main__":
    unittest.main()
