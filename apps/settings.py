class DevConfig:
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = "sqlite:///Elm.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "AABBCC"
