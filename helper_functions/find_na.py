import pandas

def find_na(df):
    print(pd.isna(df).sum())
