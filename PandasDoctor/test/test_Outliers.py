import unittest
import pandas as pd
import numpy as np
from PandasDoctor.evaluators import eval_outliers

class TestOutliers(unittest.TestCase):

    def setUp(self):
        #bad column
        x = np.random.normal(0, 0.5, 100-3)
        #good column
        y = np.random.normal(0, 0.5, 100)
        # Add three outliers to X column
        x = np.r_[x, -3, -10, 12]
        self.x = pd.DataFrame({'col1':x,'col2':y})

    def test(self):
        self.assertTrue(eval_outliers(self.x,['col1']))
        self.assertFalse(eval_outliers(self.x,'col2'))
        self.assertTrue(eval_outliers(self.x,'col1',method='iqr'))
        self.assertTrue(eval_outliers(self.x,['col1','col2']))

if __name__ == "__main__":
    unittest.main()
