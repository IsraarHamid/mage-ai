from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.s3 import S3
import pandas as pd
from os import path
from minio import Minio
from minio.error import S3Error
from io import StringIO

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_s3(df: pd.DataFrame, **kwargs) -> None:
    """
    Exporting data to a S3 bucket.
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

    # Make  bucket if not exist.
    found = client.bucket_exists("izisamples")
    if not found:
        client.make_bucket("izisamples")
    else:
        print("Bucket 'izisamples' already exists")

    df.to_csv("recipe_data.csv")

    client.fput_object(
        "izisamples", "recipe_data.csv", "/home/israar/mage-ai/recipe_data.csv",
    )
