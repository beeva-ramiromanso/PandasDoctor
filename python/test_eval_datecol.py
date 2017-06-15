import pandas as pd
import eval_datecol as t

def generate_example():
    # Generate some data
    x = pd.DataFrame({"col1":["2003-12-23","2003-12-25","2003-12-28"],
                      "col2":["2003-12-23","2003-12-25","2003-12-28"]
                      })
    #Add three outliers...
    y = pd.DataFrame({"col1":["2003-12-232","2003-112-23","2003-12-23a"],
                      "col2":["2003-12-23","2003-12-25","2003-12-28"]
                      })
    x = x.append(y,ignore_index=True)
    #x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    print(t.eval_datecol(x,['col1','col2']))
