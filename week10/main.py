import os
from flask import Flask
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig, TestingConfig
from application.database import db
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.models import User, Role
# what the hell

app = None
api = None

def create_app():
    app = Flask(__name__, template_folder="templates")
    if os.getenv('ENV', "development") == "production":
      raise Exception("Currently no production config is setup.")
    elif os.getenv('ENV', "testing") == "testing":
        app.logger.info("Starting testing")
        print("starting testing")
        app.config.from_object(TestingConfig)
    else:
      print("Staring Local Development")
      app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    api = Api(app)
    app.app_context().push()
    user_datastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
    security = Security(app, user_datastore)
    return app, api

app, api = create_app()

# Import all the controllers so they are loaded
from application.controllers import *

@app.errorhandler(404)
def page_not_found(e):
   return render_template('404.html'), 404  

@app.errorhandler(403)
def forbidden(e):
   return render_template('403.html'), 403

from application.api import UserAPI
api.add_resource(UserAPI,"/api/user", "/api/user/<string:username>")

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
  # Run the Flask app
  app.run(host='0.0.0.0',port=8081)
