import pandas as pd
import pandasql as ps

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df: pd.DataFrame, *args, **kwargs):
    """
    Code for a transformer block for agent_collection_report.csv report.
    Args:
        df: The output from the upstream parent block

    Returns:
        csv report file
    """

    filename = 'agent_collection_report'

    payments = df

    q1 = """SELECT * FROM payments """

    print(ps.sqldf(q1, locals()))
    data = ps.sqldf(q1, locals())

    return data, filename


@test
def test_output(output, *args) -> None:
    """
    Unit test for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
