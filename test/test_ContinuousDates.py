import unittest
import pandas as pd
from PandasDoctor.evaluators import eval_continuous_date

class TestContinuousDates(unittest.TestCase):

    def setUp(self):
        # Generate some data
        x = pd.DataFrame({"col1":["2003-12-23","2003-12-24","2003-12-25"],
                          "col2":["2003-12-23","2003-12-24","2003-12-25"],
                          "col3":["2003-12-23","2003-12-24","2003-12-25"],
                          })
        #Add three outliers...
        y = pd.DataFrame({"col1":["2003-12-26","2003-12-27","2003-12-28"],
                          "col2":["2003-12-26","2003-12-28","2003-12-27"],
                          "col3":["2003-12-26","2003-12-28","2003-12-30"]
                          })
        self.x = x.append(y,ignore_index=True)

    def test(self):
        self.assertFalse(eval_continuous_date(self.x,['col1']))
        self.assertFalse(eval_continuous_date(self.x,'col2'))
        self.assertTrue(eval_continuous_date(self.x,'col3'))
        self.assertTrue(eval_continuous_date(self.x,['col1','col2','col3']))

if __name__ == "__main__":
    unittest.main()
