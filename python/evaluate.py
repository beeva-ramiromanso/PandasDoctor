

def evaluate(df,type="all", *args, **kwargs):
    #identiy numeric columns
    ind = list(df.select_dtypes(include=[np.number]).columns.values)

    # default mode in R outliers package is z-scores => (x-mean)/sd

    res = list()
    for col in ind:
        tmp = z_score(df[col])
        out = np.sum(tmp)
        if out > 0:
            res.append(tmp)
            print("{0} Outliers found in var {1}".format(out,col))
        else:
            print("No outliers found in var {0}".format(col))

    return(res)
