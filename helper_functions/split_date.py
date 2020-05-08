
import pandas as pd

def split_date(df, date_column):
        """
        Function
        ________
            Expands pandas dataframe date column into 'Year', 'Month', 'Day'

        Params
        __________
            args:
                df(pd.DataFrame) : df to modify
                date_column(String) : column name of the date column to expand

        Return
        ______
            Returns a copy of passed df with df['Year'], df['Month'], and df['Day'] columns
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
