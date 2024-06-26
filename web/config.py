# pylint: disable=invalid-name
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


class BaseConfig(object):
    def __init__(self) -> None:
        self.DB_HOST_NAME = os.environ["DB_HOST_NAME"]
        self.DB_PASS = os.environ["DB_PASS"]
        self.DB_PORT = os.environ["DB_PORT"]
        self.DEBUG = os.environ["DEBUG"]
        self.DB_NAME = os.environ["DB_NAME"]
        self.DB_USER = os.environ["DB_USER"]
        self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST_NAME}:{self.DB_PORT}/{self.DB_NAME}"
        self.SQLALCHEMY_TRACK_MODIFICATION = False


class BaseConfigLocal(BaseConfig):
    def __init__(self):
        super().__init__()
        self.DB_HOST_NAME = os.environ["LOCAL_DB_HOST_NAME"]
        self.SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST_NAME}:{self.DB_PORT}/{self.DB_NAME}"
