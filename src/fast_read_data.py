import pyarrow.feather as feather
import numpy as np
from pyarrow import csv
import pandas as pd
import time

def construct_arr(path,r,c,to):
    df = pd.read_csv(path)
    arr = np.zeros((r,c))
    for i in range(len(df)):
        x = int(df.iloc[i]["X"])
        y = int(df.iloc[i]["Y"])
        val = df.iloc[i]["TF-IDF"]
        arr[x][y] = val

    pd.DataFrame(arr).to_csv(to)



def write_pandas_to_feather(path,to):
    start = time.time()
    df = pd.read_csv(path)
    end = time.time()
    print(end - start)
    # df.loc[:20].reset_index().to_feather(to)

def fast_read(path,r,c):
    read_df = pd.read_feather(path)
    print("done with importing data")
    arr = np.zeros((r,c))

    for i in range(len(read_df)):
        x = int(read_df.iloc[i]["X"])
        y = int(read_df.iloc[i]["Y"])
        val = read_df.iloc[i]["TF-IDF"]
        arr[x][y] = val


    print("done with setting values")