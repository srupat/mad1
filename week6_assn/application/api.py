from flask_restful import Resource, fields, marshal_with
from application.database import db
from application.models import User, Article
from application.validation import NotFoundError
from flask_restful import reqparse
from application.validation import BusinessValidationError

class UserAPI():
    something