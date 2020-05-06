import pandas as pd

def find_na(df):
    print(pd.isna(df).sum())


df = pd.DataFrame({"a":[1,None,2], "b":[None, None, 4]})

find_na(df)
