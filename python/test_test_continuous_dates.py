import pandas as pd
import test_continuous_date as t

def generate_example():
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
    x = x.append(y,ignore_index=True)
    #x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    print(t.test_continuous_date(x,['col1','col2','col3']))
