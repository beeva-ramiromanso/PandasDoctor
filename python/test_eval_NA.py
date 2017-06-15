import pandas as pd
import eval_NA as t

def generate_example():
    # Generate some data
    x = pd.DataFrame({"col1":["A","B","C"],
                      "col2":["D","E","F"],
                      "col3":[1,2,3],
                      "col4":["D","E","F"]})
    # Add three outliers...
    y = pd.DataFrame({"col1":["NA","NULL","C"],
                      "col2":["D","-999","999"],
                      "col3":[999,-999,3],
                      "col4":["D",None,"F"]})
    x = x.append(y,ignore_index=True)
    #x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    t.evaluate_NA(x,['col1','col2','col3','col4'],print_invalid=True)
