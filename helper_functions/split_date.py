
import pandas as pd

def split_date(df, date_column):
    """
    split_date(df, date_column)
        -df - pandas DataFrame
        -date_column - date column to split
    Split df['date'] column into Year, Month, Day columns
    """
    try:
        split_df = df.copy()

    except:
        return "df needs to be a pandas.DataFrame"

    try:
        split_df['Year'] = pd.DatetimeIndex(df[date_column]).year
        split_df['Month'] = pd.DatetimeIndex(df[date_column]).month
        split_df['Day'] = pd.DatetimeIndex(df[date_column]).day

        return split_df.drop(columns=[date_column])

    except:
        return "date_column passed is not datetime"
