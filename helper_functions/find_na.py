import pandas as pd

def find_na(df):
    print(pd.isna(df).sum())
