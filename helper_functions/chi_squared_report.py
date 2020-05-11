from scipy.stats import chi2_contingency
import pandas as pd

def chi_squared_report(df, col1, col2):
    """
    Function
    ________
        Prints  - a cross tab of a given two columns of a pandas.DataFrame
                - chi2, p-value, dof, and expected frequencies

    Params
    __________
        args:
            df(pd.DataFrame) : df to modify
            col1(String) : column name of the df
            col2(String) : column name of the df

    Return
    ______
        None
    """

    try:
        observed = pd.crosstab(df[col1], df[col2], margins=False)
        print("contingency table:")
        print(observed)
        print("\n")

        chi2, p_value, dof, expected = chi2_contingency(observed)

        print(f"chi2: {chi2}")
        print(f"p-value: {p_value}")
        print(f"dof: {dof}")
        print(f"\nexpected frequncy:\n {expected}")

    except Exception as e:
        print(e)




if __name__ == "__main__":
    #
    # df = pd.DataFrame({"a":["bat", "cat", "bat"], "b":["home", "away", "away"]})
    #
    # # print(df)
    # # print("\n\n\n")
    # # print(pd.crosstab(df["a"], df["b"], margins=True))
    #
    # chi_squared_report(df, "a", "b")
