
import numpy as np
import pandas as pd


def add_state_names(df, state_column, direction=None):
    """
    Function
    ________
        Translates a pandas dataframe state column into corresponding full_name or abbreviation

    Params
    __________
        args:
            df(pd.DataFrame) : df to modify returns copy with states_translated column
            state_column(String) : column name of the state column to df_translate

        kwargs:
            direction : direction to translate.
                    "abreviate" -> California to CA
                    "full" -> CA to California
                    None -> random samples to guess direction

    Return
    ______
        Returns a copy of passed df with df['states_translated'] column
    """

    # copy DataFrame
    df_translated = df.copy()

    # states dict
    states_dict = {"Alabama": "AL",
                   "Alaska":	"AK",
                   "Arizona": "AZ",
                   "Arkansas": "AR",
                   "California":	"CA",
                   "Colorado": "CO",
                   "Connecticut": "CT",
                   "Delaware": "DE",
                   "District of Columbia": "DC",
                   "Florida":"FL",
                   "Georgia": "GA",
                   "Hawaii": "HI",
                   "Idaho": "ID",
                   "Illinois": "IL",
                   "Indiana": "IN",
                   "Iowa": "IA",
                   "Kansas":	"KS",
                   "Kentucky": "KY",
                   "Louisiana":	"LA",
                   "Maine":	"ME",
                   "Maryland":	"MD",
                   "Massachusetts":	"MA",
                   "Michigan":	"MI",
                   "Minnesota":	"MN",
                   "Mississippi":	"MS",
                   "Missouri":	"MO",
                   "Montana":	"MT",
                   "Nebraska":	"NE",
                   "Nevada":	"NV",
                   "New Hampshire":	"NH",
                   "New Jersey":	"NJ",
                   "New Mexico":	"NM",
                   "New York":	"NY",
                   "North Carolina":	"NC",
                   "North Dakota":	"ND",
                   "Ohio":	"OH",
                   "Oklahoma":	"OK",
                   "Oregon":	"OR",
                   "Pennsylvania":	"PA",
                   "Rhode Island":	"RI",
                   "South Carolina":	"SC",
                   "South Dakota":	"SD",
                   "Tennessee":	"TN",
                   "Texas":	"TX",
                   "Utah":	"UT",
                   "Vermont":	"VT",
                   "Virginia":	"VA",
                   "Washington":	"WA",
                   "West Virginia":	"WV",
                   "Wisconsin":	"WI",
                   "Wyoming":	"WY",
                   "Puerto Rico":	"PR"
                   }


    # excute translation per direction
    if direction == "abbreviate":
        df_translated[state_column] = df_translated[state_column].str.title()
        df_translated['states_translated'] = df_translated[state_column].map(states_dict)

    elif direction == "full":
        states_dict =  {v : k for k, v in states_dict.items()}
        df_translated[state_column] = df_translated[state_column].str.upper()

        df_translated['states_translated'] = df_translated[state_column].map(states_dict)

    # sample df to guess direction if None
    else:
        if len(df_translated['state']) < 10:
            sample_len = len(df_translated['state'])
        else:
            sample_len = 10
        sample = df_translated['state'].sample(sample_len).values

        avg_len = 0
        for x in sample:
            avg_len += len(x)
        avg_len/=sample_len

        if avg_len >= 4:
            df_translated[state_column] = df_translated[state_column].str.title()
            df_translated['states_translated'] = df_translated[state_column].map(states_dict)

        else:
            states_dict = {v: k for k, v in states_dict.items()}
            df_translated[state_column] = df_translated[state_column].str.upper()
            df_translated['states_translated'] = df_translated[state_column].map(states_dict)

    return df_translated


# if __name__ == "__main__":
#
#     my_df = pd.DataFrame({"state": ["Al", "Tx", "IN"], "city": ["Montgomery", "Dallas", "Indianappolis"]})
#
#     print(add_state_names(my_df, "state"))
