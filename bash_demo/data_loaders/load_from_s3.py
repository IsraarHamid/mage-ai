from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
from os import path
from minio import Minio
from minio.error import S3Error
import pandas as pd
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_s3_bucket(*args, **kwargs):
    """
    Use MINIO.

    Docs: https://docs.mage.ai/design/data-loading#s3
    """
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        "play.min.io",
        access_key="eSbIw0JJQZBC7u2o",
        secret_key="0kRLxXXceG8m7Yt2VLl2vpsIKRhGC6tV",
    )

    csv_file = client.get_object("izisamples", "recipe_data.csv", "recipe_data.csv")

    df = pd.read_csv(csv_file)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
