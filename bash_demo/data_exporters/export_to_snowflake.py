from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
import pandas as pd
from os import path
from snowflake.connector.pandas_tools import pd_writer
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
import functools
import datetime as dt

registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_snowflake(df: pd.DataFrame, **kwargs) -> None:
    """
    Export DataFrame data to a Snowflake warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    account_identifier = 'kjlcjth-zn58087'
    user = 'Israar'
    password = 'Israar$n0w'
    database_name = 'TEST'
    schema_name = 'RAW'

    conn_string = f"snowflake://{user}:{password}@{account_identifier}/{database_name}/{schema_name}"
    engine = create_engine(conn_string)

    table_name = 'recipes_raw'

    if_exists = 'replace'

    #Write and modify the data to Snowflake, using pd_writer to speed up loading
    df['updated_at'] = pd.Timestamp('now').strftime("%Y/%m/%d %H:%M:%S")
    df = df.drop(['Unnamed: 0'], axis=1)

    df.to_sql(name=table_name.lower(), con=engine, if_exists=if_exists, method=functools.partial(pd_writer, quote_identifiers=False), index=False)
