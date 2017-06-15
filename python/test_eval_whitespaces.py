import pandas as pd
import eval_whitespaces as t

def generate_example():
    # Generate some data
    x = pd.DataFrame({"col1":["AA","BB","CC"],
                      "col2":["DAA","EEEE","FFFF"]
                      })
    # Add three outliers...
    y = pd.DataFrame({"col1":["AAAA","BBB","CCC"],
                      "col2":["DAA "," AAAA"," AA "]
                      })
    x = x.append(y,ignore_index=True)
    #x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    print(t.eval_whitespaces(x,['col1']))
    print(t.eval_whitespaces(x,['col2'],print_invalid=True))
