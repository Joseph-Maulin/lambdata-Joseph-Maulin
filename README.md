# lambdata-Joseph-Maulin
3.2 package


## Installation
pip install -i https://test.pypi.org/simple/ lambdata-Joseph-Maulin


## Usage
```py
  from helper_functions.helper import Helper

  df = pd.DataFrame({"state":["AL", "Tx", "IN"], "city":["Montgomery", "Dallas", "Indianappolis"], "date":[2020-01-02, 2020-04-03, 2020-05-10]})

  helper = Helper(df)

  helper.add_state("state", direction=None)
  helper.split_date("date")

  df = helper.get_df()
```


# These can be called outside Helper(). Inside method helper argument df == self.

```py
from helper_functions.state_abreviation import add_state_names

def add_state_names(df, state_column, direction=None):
    """
        df(pd.DataFrame) : df to modify returns copy with states_translated column
        state_column(String) : column name of the state column to df_translate
        direction : direction to translate.
                    "abreviate" -> California to CA
                    "full" -> CA to California
                    None -> random sample to guess direction
    """

my_df = pd.DataFrame({"state":["AL", "Tx", "IN"], "city":["Montgomery", "Dallas", "Indianappolis"]})
add_state_names(df, state_column)

print(add_state_names(my_df, "state"))

```

```py
from helper_functions.split_date import split_date

df = pd.DataFrame({"date":["2020-01-01"]})
print(split_date(df, "date"))
```



```py
from helper_functions.chi_squared_report import chi_squared_report

def chi_squared_report(df, col1, col2):
    """
        vars:
            df - dataframe
            col1 - col1
            col2 - col2

        description:
            print contingency table and chi-test result
    """

    df = pd.DataFrame({"a":["bat", "cat", "bat"], "b":[1, 4, 4]})

    chi_squared_report(df, "a", "b")

```
