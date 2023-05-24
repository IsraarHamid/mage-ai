from mage_ai.io.file import FileIO
from pandas import DataFrame

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_file(df: DataFrame, filename: str **kwargs) -> None:
    """
    Export csv data to folder.
    Note: Point filepath variable to directory path of folder for demo.

    Docs: https://docs.mage.ai/design/data-loading#fileio
    """
    folder_name = 'output_folder'

    filepath = f"/home/israar/mage-ai/lumkani/{folder_name}/{filename}.csv"
    
    FileIO().export(df, filepath)
