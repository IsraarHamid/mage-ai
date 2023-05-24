import pandas as pd
import pandasql as ps

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Code for a transformer block for days_from_suspension_report.csv report.
    Args:
        data: The output from the upstream parent block

    Returns:
        csv report file
    """

    filename = 'days_from_suspension_report'

    q1 = """SELECT ID FROM df """

    print(ps.sqldf(q1, locals()))

    return data, filename


@test
def test_output(output, *args) -> None:
    """
    Unit test for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
