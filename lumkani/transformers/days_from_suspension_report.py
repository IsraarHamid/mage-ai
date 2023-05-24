import pandas as pd
import pandasql as ps

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: pd.DataFrame, *args, **kwargs):
    """
    Code for a transformer block for days_from_suspension_report.csv report.
    Args:
        df: The output from the upstream parent block

    Returns:
        csv report file
    """

    payments = df

    q1 = """
    SELECT t.device_id, r.created, 
    JULIANDAY(r.created) - JULIANDAY(DATETIME(r.created, '+90 days')) 
    AS days_from_suspension
    FROM (
        SELECT device_id, MAX(created) as created
        FROM payments
        GROUP BY device_id
    ) r
    INNER JOIN payments t
    ON t.device_id = r.device_id AND t.created = r.created
    
    """

    data = ps.sqldf(q1, locals())

    return data


@test
def test_output(output, *args) -> None:
    """
    Unit test for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
