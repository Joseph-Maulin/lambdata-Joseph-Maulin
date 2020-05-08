# lambdata-Joseph-Maulin
3.1 package


## Installation
pip install -i https://test.pypi.org/simple/ lambdata-Joseph-Maulin


## Usage
```py
from helper_functions.state_abreviation import add_state_names

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
