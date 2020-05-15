
# todo
# Class is not finished

class Helper:

    def __init__(self, df):
        self.df = df

    def __re__(self):
        pass

    def add_state_names(self, state_column, direction=None):
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
        df_translated = self.df.copy()

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

        self.df = df_translated


    def split_date(self, date_column):
        """
        Function
        ________
            Expands pandas dataframe date column into 'Year', 'Month', 'Day'

        Params
        __________
            args:
                date_column(String) : column name of the date column to expand

        Return
        ______
            Returns a copy of passed df with df['Year'], df['Month'], and df['Day'] columns
        """
        try:
            split_df = self.df.copy()

        except:
            return "df needs to be a pandas.DataFrame"

        try:
            split_df['Year'] = pd.DatetimeIndex(df[date_column]).year
            split_df['Month'] = pd.DatetimeIndex(df[date_column]).month
            split_df['Day'] = pd.DatetimeIndex(df[date_column]).day

            self.df = split_df.drop(columns = [date_column])
            return self.df

        except:
            return "date_column passed is not datetime. self.df is unchanged"

    def get_df(self):
        return self.df
