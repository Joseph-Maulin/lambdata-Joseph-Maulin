from scipy.stats import chi2_contingency
import pandas as pd

def chi_squared_report(df, col1, col2):
    """
        vars:
            df - dataframe
            col1 - col1
            col2 - col2

        description:
            print contingency table and chi-test result
    """

    observed = pd.crosstab(df[col1], df[col2], margins=False)
    print("contingency table:")
    print(observed)
    print("\n")

    chi2, p_value, dof, expected = chi2_contingency(observed)

    print(f"chi2: {chi2}")
    print(f"p-value: {p_value}")
    print(f"dof: {dof}")
    print(f"\nexpected frequncy:\n {expected}")





df = pd.DataFrame({"a":["bat", "cat", "bat"], "b":[1, 4, 4]})

# print(df)
# print("\n\n\n")
# print(pd.crosstab(df["a"], df["b"], margins=True))

chi_squared_report(df, "a", "b")
