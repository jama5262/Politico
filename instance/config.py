import os


class Config:
    DEBUG = False
    JAMA = "JAMA MOHAMED WARDERE"


class DevelopmentConfig(Config):
    DEBUG = True
    JAMA = "JAMA MOHAMED WARDERE"


class TestingConfig(Config):
    TESTING = True
    DEBUG = True


appConfig = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
}
