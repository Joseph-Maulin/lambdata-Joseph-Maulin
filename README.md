# lambdata-Joseph-Maulin
3.1 package


## Installation
pip install -i https://test.pypi.org/simple/ lambdata-Joseph-Maulin


## Usage
```py
from helper_functions.state_abreviation import state_abreviation

print(state_abreviation("IN"))

```

```py
from helper_functions.split_date import split_date

df = pd.DataFrame({"date":["2020-01-01"]})
print(split_date(df, "date"))
```
