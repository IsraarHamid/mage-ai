from mage_ai.io.file import FileIO
from pandas import DataFrame
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, **kwargs) -> None:
    """
    Export csv data to folder.
    
    Notes: 
    Update directory path of folder for demo.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    folder_name = 'output_folder'

    dir_path = '/home/israar/mage-ai/lumkani/'

    # Create directory if not exists
    if not os.path.exists(f"{dir_path}{folder_name}"):
        os.makedirs(f"{dir_path}{folder_name}")
    else: print("Directory exists.")

    filename = 'agent_collection_report'

    filepath = f"{dir_path}{folder_name}/{filename}.csv"

    FileIO().export(df, filepath)
