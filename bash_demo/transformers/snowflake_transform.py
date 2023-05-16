from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.snowflake import Snowflake
from snowflake.connector import connect
from sqlalchemy import create_engine
from sqlalchemy.dialects import registry
import functools

registry.register('snowflake', 'snowflake.sqlalchemy', 'dialect')
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Transform Snowflake data and create views.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#snowflake
    """
    account_identifier = 'kjlcjth-zn58087'
    user = 'Israar'
    password = 'Israar$n0w'
    database_name = 'TEST'
    schema_name = 'RAW'

    conn = connect(
        user=user,
        password=password,
        account=account_identifier
    )

    recipe_sql = """
    CREATE 
    OR REPLACE VIEW TEST.PRD.RECIPE AS 
    SELECT 
    * 
    FROM 
    TEST.RAW.RECIPES_RAW;
    """

    batter_sql = ''

    topping_sql = ''

    cursor = conn.cursor()
    cursor.execute(recipe_sql)
    cursor.close()
