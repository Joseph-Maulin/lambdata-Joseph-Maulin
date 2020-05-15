

import unittest
import pandas as pd

from helper_functions.helper import Helper


class TestHelper(unittest.TestCase):

    def test_state_abreviation(self):

        df = pd.DataFrame({"state":['CA','in']})
        helper = Helper(df)

        helper.add_state_names("state", direction='full')

        state_values = list(helper.get_df()['states_translated'].values)
        print(state_values)

        self.assertEqual(state_values[0], "California")
        self.assertEqual(state_values[1], "Indiana")



if __name__ == '__main__':
    unittest.main()
