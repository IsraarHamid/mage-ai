import pandas as pd
import glob
import os

from mage_ai.io.file import FileIO
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_file(*args, **kwargs):
    """
    Load multiple csv files into singular DataFrame.

    Note: Point path_to_csv variable to directory path for demo.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    path_to_csv = '/home/israar/mage-ai/lumkani/sample_data/' 
    csv_pattern = os.path.join(path_to_csv,'*.csv')

    file_list = glob.glob(csv_pattern)

    temp = pd.DataFrame()

    dfs = [] # An empty list to store the DataFrames

    for file in file_list:
        data = pd.read_csv(file, skip_blank_lines=True) # Read data frame from the csv file
        
        # Data input limit validation

        if len(data) <= 100000:
            dfs.append(data) # Append the DataFrames to the list
        else:
            print("Data input exceeds data limit of 100 000 records.")

    temp = pd.concat(dfs, ignore_index=True) # Concatenate all the data frames in the list.
    
    return temp


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'