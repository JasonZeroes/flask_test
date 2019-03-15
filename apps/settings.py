import os

from redis import Redis


def get_db_path():
    path = os.path.dirname(os.path.dirname(__file__))
    return f"sqlite:///{path}/Elm.db"


class DevConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = get_db_path()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ABC"

    SESSION_TYPE = "redis"
    SESSION_REDIS = Redis(host="127.0.0.1", port=6379)
    SESSION_KEY_PREFIX = "2019:"
