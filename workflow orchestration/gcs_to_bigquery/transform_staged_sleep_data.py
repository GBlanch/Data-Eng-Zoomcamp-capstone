if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data.columns = data.columns.str.lower()
    data.drop('blood_pressure',
               axis = 1,
               inplace = True)

    return data


