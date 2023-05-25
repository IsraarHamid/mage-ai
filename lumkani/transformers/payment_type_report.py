import pandas as pd
import pandasql as ps
from datetime import date

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: pd.DataFrame, *args, **kwargs):
    """
    Code for a transformer block for payment_type_report.csv report.
    Args:
        df: The output from the upstream parent block

    Returns:
        csv report file
    """

    payments = df

    today = date.today()

    q1 = f"""
    SELECT t.device_id, 
    CASE WHEN STRFTIME("%Y-%m", {today}) = STRFTIME("%Y-%m", r.created)
    THEN JULIANDAY(DATETIME(r.created, '+90 days')) - JULIANDAY(r.created)
    ELSE 0 END
    AS days_from_suspension
    FROM (
        SELECT device_id, MAX(created) as created
        FROM payments
        GROUP BY device_id
    ) r
    INNER JOIN payments t
    ON t.device_id = r.device_id AND t.created = r.created
    order by 2 desc
    """

    data = ps.sqldf(q1, locals())

    return data


@test
def test_output(output, *args) -> None:
    """
    Unit test for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
