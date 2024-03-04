if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import numpy as np
import pandas as pd

@transformer
def transform(data, *args, **kwargs):

    # To make data handling less cumbersome, replace spaces with underscores
    data.columns = [spaces.replace(' ', '_') for spaces in data.columns] 

    # Unify 'Normal' and 'Normal weight' weight
    data["BMI_Category"] = data["BMI_Category"]\
                           .apply(lambda x: x.replace("Normal Weight",
                                                      "Normal"))
    # impute NaNs
    data = data.replace(np.nan, 'None',
                         regex = True)


    data[['Systolic_BP', 'Diastolic_BP']] = data["Blood_Pressure"]\
                                          .apply(lambda x: pd.Series(str(x)\
                                                                    .split("/")))

    return data


@test
def test_output(output, *args):
    """
    Template code for testing the output of the block.
    """
    assert output.isnull()\
                 .sum().any() == False, 'NaNs still exist in the dataframe'