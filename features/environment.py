import os
from glob import glob

from behave import fixture, use_fixture
from requests_toolbelt.sessions import BaseUrlSession

import app


@fixture
def data_dir(context, *args, **kwargs):
    context.data_dir = "test_data"
    yield context.data_dir
    for file in glob(f"{context.data_dir}/*.json"):
        os.remove(file)


@fixture
def fastapi_client(context, *args, **kwargs):
    app.DATA_DIR = context.data_dir
    context.client = BaseUrlSession(base_url="http://localhost:8082")
    yield context.client


def before_feature(context, feature):
    use_fixture(data_dir, context)
    use_fixture(fastapi_client, context)
