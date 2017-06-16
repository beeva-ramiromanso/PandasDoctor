import unittest
import pandas as pd
from PandasDoctor.evaluators import eval_datecol

class TestDateCols(unittest.TestCase):

    def setUp(self):
        # Generate some data
        x = pd.DataFrame({"col1":["2003-12-23","2003-12-25","2003-12-28"],
                          "col2":["2003-12-23","2003-12-25","2003-12-28"]
                          })
        #Add three outliers...
        y = pd.DataFrame({"col1":["2003-12-232","2003-112-23","2003-12-23a"],
                          "col2":["2003-12-23","2003-12-25","2003-12-28"]
                          })
        self.x = x.append(y,ignore_index=True)

    def test(self):
        self.assertTrue(eval_datecol(self.x,['col1']))
        self.assertFalse(eval_datecol(self.x,'col2'))
        self.assertTrue(eval_datecol(self.x,['col1','col2']))

if __name__ == "__main__":
    unittest.main()
