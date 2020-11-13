import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
def load_and_process(path):
    df1 = (pd
           .read_csv(path)
           .dropna(how='any')
           .rename(columns={"created_at":"time_start", "last_move_at":"time_end"})
           .sort_values("turns", ascending=True)
          )
    df2 = (df1
           .assign(date_start=(pd.to_datetime(df1["time_start"])))
           .assign(date_end=(pd.to_datetime(df1["time_end"])))
          )
    df3 = (df2
           .assign(length=(df2["date_end"] - df2["date_start"])*10000000)
           .drop(columns=["white_id",
                          "id",
                          "black_id",
                          "increment_code",
                          "time_start",
                          "time_end",
                          "rated"])
          )
    return df3