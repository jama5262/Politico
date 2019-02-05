from flask import Flask
from instance.config import appConfig

def createApp (configName):
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_object(appConfig[configName])
  app.config.from_pyfile('config.py')
  return app