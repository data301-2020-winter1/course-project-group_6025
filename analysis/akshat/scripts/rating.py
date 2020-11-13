import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def modify(df):
    abs_rating = pd.Series([])
    
    for i in range(len(df)):
        abs_rating[i] = abs(df["white_rating"][i] - df["black_rating"][i])
   
    (df.insert(4, "absolute_rating", abs_rating))

    return df