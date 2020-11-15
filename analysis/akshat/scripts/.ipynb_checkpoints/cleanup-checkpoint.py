import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def clean(path):
    df_base = (pd
        .read_csv(path)
        .dropna(how = 'any')
        
    )

    df_reduced = (df_base
                    .drop(columns=["white_id", "id", "victory_status", "increment_code", "black_id", "turns", "created_at", "last_move_at"])            
    )
    return df_reduced
