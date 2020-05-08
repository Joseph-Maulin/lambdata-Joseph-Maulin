
import numpy as np
import pandas as pd



def add_state_names(df, state_column, direction=None):
    """
        df(pd.DataFrame) : df to modify returns copy with states_translated column
        state_column(String) : column name of the state column to df_translate
        direction : direction to translate.
                    "abreviate" -> California to CA
                    "full" -> CA to California
                    None -> random sample to guess direction
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
    if direction == "abreviate":
        df_translated[state_column] = df_translated[state_column].str.title()
        df_translated['states_translated'] = df_translated[state_column].map(states_dict)

    elif direction == "full":
        states_dict =  {v: k for k, v in states_dict.items()}
        df_translated[state_column].str.upper()

        df_translated['states_translated'] = df_translated[state_column].map(states_dict)

    # sample df to guess direction if None
    else:
        sample = df_translated.sample(10)



    return df_translated





if __name__ == "__main__":

    my_df = pd.DataFrame({"state":["AL", "Texas", "IN"], "city":["Montgomery", "Dallas", "Indianappolis"]})
    #
    # print(add_state_names(my_df, "state"))

    avg_len = 0
    for x in my_df['state'].values:
        avg_len += len(x)

    avg_len /= len(my_df['state'])
