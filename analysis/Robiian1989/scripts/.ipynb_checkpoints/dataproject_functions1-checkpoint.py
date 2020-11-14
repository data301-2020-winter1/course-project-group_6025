import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_process(path):

#loading data and removing nan values

    df1=(pd.read_csv("../../data/raw/Dataset_irobinson.csv.csv")
         .dropna()
   )
    df2= (df1.drop(['created_at','last_move_at','rated','white_id','black_id'],axis=1)
        .dropna()
        .sort_values(by=['turns'],ascending=True)
        .assign(move_name_and_eco= df['opening_name']+ '('+ df['opening_eco'] +')')
        .drop(['opening_eco','opening_name'],axis=1)
        .rename(columns={'increment_code':'time'})
        .reset_index(drop=True)
)
    return df2