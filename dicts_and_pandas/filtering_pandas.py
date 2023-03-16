import pandas as pd
import numpy as np

brics = pd.read_csv("dicts_and_pandas/brics.csv", index_col=0)

#is_huge = brics["area"] > 8

is_huge = brics[brics["area"] > 8]

print(brics[np.logical_and(brics["area"] > 8, brics["area"] < 10)])


#print(is_huge)
