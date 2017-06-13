import test_outliers as t
import pandas as pd
import numpy as np

def generate_example(n=100):
    # Generate some data
    x = np.random.normal(0, 0.5, n-3)
    # Add three outliers...
    x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    y = generate_example()
    d = pd.DataFrame({'example':x,'example2':y})
    t.detect_outliers(d)
