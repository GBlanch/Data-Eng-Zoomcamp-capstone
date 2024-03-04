import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://raw.githubusercontent.com/GBlanch/DTC-Data-Eng.-capstone-project/main/dataset/Sleep_health_and_lifestyle_dataset.csv'

    sleep_health_type = {

        'Person_ID' : pd.Int64Dtype() ,
        'Gender' : str,
        'Age' : pd.Int64Dtype(),
        'Occupation' : str,
        'Sleep_Duration' : float ,
        'Quality_of_Sleep' : pd.Int64Dtype() ,
        'Physical_Activity_Level' : pd.Int64Dtype(),
        'Stress_Level' : pd.Int64Dtype(),
        'BMI_Category' : str,
        'Blood_Pressure' : str,
        'Heart_Rate' : pd.Int64Dtype(),
        'Daily_Steps' : pd.Int64Dtype(),
        'Sleep_Disorder' : str

    }

    return pd.read_csv(url, 
                       sep = ',',
                       dtype = sleep_health_type
    )

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
