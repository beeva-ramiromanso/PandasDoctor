import pandas as pd
import test_NA as t

def generate_example():
    # Generate some data
    x = pd.DataFrame({"col1":["A","B","C"],
                      "col2":["D","E","F"],
                      "col3":[1,2,3]})
    # Add three outliers...
    y = pd.DataFrame({"col1":["NA","NULL","C"],
                      "col2":["D","-999","999"],
                      "col3":[999,-999,3]})
    x = x.append(y,ignore_index=True)
    #x = np.r_[x, -3, -10, 12]
    return(x)

if __name__ == "__main__":
    x = generate_example()
    t.test_for_NA(x)
    print(x)


    # x = generate_example()
    # y = generate_example()
    # d = pd.DataFrame({'example':x,'example2':y})
    # t.detect_outliers(d)
