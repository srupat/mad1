import os
from application import config
from application.config import LocalDevelopmentConfig
from flask import Flask
from flask_restful import Api
from flask import render_template
from flask import request
from sqlalchemy.orm import scoped_session
from application.database import db

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    else:
      print("Starting Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    return app, api

app, api = create_app()

from application.controllers import *

if __name__ == "__main__":
    app.run()