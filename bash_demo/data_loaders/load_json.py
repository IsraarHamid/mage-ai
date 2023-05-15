import pandas as pd
import glob
import os, json

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Load multiple json files into singular DataFrame.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    path_to_json = '/sample_data/*' 
    json_pattern = os.path.join(path_to_json,'*.json')
    file_list = glob.glob(json_pattern)

    temp = pd.DataFrame()

    dfs = [] # An empty list to store the DataFrames

    for file in file_list:
        data = pd.read_json(file, lines=True) # Read data frame from the json file
        dfs.append(data) # Append the DataFrames to the list

    temp = pd.concat(dfs, ignore_index=True) # Concatenate all the data frames in the list.
    print(temp)
    return temp


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
