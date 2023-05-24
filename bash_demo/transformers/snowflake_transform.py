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

    batter_sql = """
    CREATE 
    OR REPLACE VIEW TEST.PRD.BATTER AS (
    WITH DATA AS (
    select 
        * 
    from 
        TEST.RAW.RECIPES_RAW
    ) 
    SELECT 
    DATA.ID AS RECIPE_ID, 
    BATTERS.value : id :: INT AS BATTER_ID, 
    BATTERS.value : type :: VARCHAR AS BATTER_TYPE, 
    DATA.UPDATED_AT 
    FROM 
    DATA, 
    LATERAL FLATTEN(
        INPUT => PARSE_JSON(DATA.BATTERS): batter, 
        OUTER => TRUE
    ) AS BATTERS
    );
    """

    topping_sql = """
    CREATE 
    OR REPLACE VIEW TEST.PRD.TOPPING AS (
    WITH DATA AS (
        select 
        * 
        from 
        TEST.RAW.RECIPES_RAW
    ) 
    SELECT 
        DATA.ID AS RECIPE_ID, 
        TOPPINGS.value : id :: INT AS TOPPING_ID, 
        TOPPINGS.value : type :: VARCHAR AS TOPPING_TYPE, 
        DATA.UPDATED_AT 
    FROM 
        DATA, 
        LATERAL FLATTEN(
        INPUT => PARSE_JSON(DATA.TOPPING), 
        OUTER => TRUE
        ) AS TOPPINGS
    );
    """

    cursor = conn.cursor()
    cursor.execute(recipe_sql)
    cursor.execute(batter_sql)
    cursor.execute(topping_sql)
    cursor.close()
