import unittest
import pandas as pd
from PandasDoctor.evaluators import eval_whitespaces

class TestWhitespaces(unittest.TestCase):

    def setUp(self):
        # Generate some data
        x = pd.DataFrame({"col1":["AA","BB","CC"],
                          "col2":["DAA","EEEE","FFFF"]
                          })
        # Add three outliers...
        y = pd.DataFrame({"col1":["AAAA","BBB","CCC"],
                          "col2":["DAA "," AAAA"," AA "]
                          })
        self.x = x.append(y,ignore_index=True)

    def test(self):
        self.assertFalse(eval_whitespaces(self.x,['col1']))
        self.assertTrue(eval_whitespaces(self.x,'col2'))
        self.assertTrue(eval_whitespaces(self.x,['col1','col2']))

if __name__ == "__main__":
    unittest.main()
