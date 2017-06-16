import unittest
import pandas as pd
from PandasDoctor.evaluators import eval_NA

class TestNA(unittest.TestCase):

    def setUp(self):
        x = pd.DataFrame({"col1":["A","B","C"],
                          "col2":["D","E","F"],
                          "col3":[1,2,3],
                          "col4":["D","E","F"],
                          "col5":["D","E","F"]
                          })
        # Add three outliers...
        y = pd.DataFrame({"col1":["NA","NULL","C"],
                          "col2":["D","-999","999"],
                          "col3":[999,-999,3],
                          "col4":["D",None,"F"],
                          "col5":["D","E","F"]
                          })
        self.x = x.append(y,ignore_index=True)

    def test(self):
        self.assertTrue(eval_NA(self.x,['col1','col2','col3','col4']))
        self.assertTrue(eval_NA(self.x,'col1'))
        self.assertFalse(eval_NA(self.x,['col5']))

if __name__ == "__main__":
    unittest.main()
