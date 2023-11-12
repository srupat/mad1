from flask_restful import Resource, fields, marshal_with
from application.database import db
from application.models import User, Article
from application.validation import NotFoundError
from flask_restful import reqparse
from application.validation import BusinessValidationError

output_fields = {
    "user_id" : fields.Integer,
    "username" : fields.String,
    "email" : fields.String
}

create_user_parser = reqparse.RequestParser()
create_user_parser.add_argument('username')
create_user_parser.add_argument('email')

update_user_parser = reqparse.RequestParser()
update_user_parser.add_argument('email')

class UserAPI(Resource):
    @marshal_with(output_fields)
    def get(self, username):
        
        # get the username
        print('In UserAPI GET Method', username)
        # get the user from database based on username
        user = db.session.query(User).filter(User.username == username).first()

        if user:
            # return a valid user json
            return user
        else:
            # return 404 error
            raise NotFoundError(status_code = 404)
        # format the return json

    @marshal_with(output_fields)
    def put(self, username):
        args = update_user_parser.parse_args()
        email = args.get('email', None)
        
        if email is None:
            raise BusinessValidationError(status_code = 400, error_code = "BE1002", error_message = "email is required")
        
        if '@' in email:
            pass
        else:
            raise BusinessValidationError(status_code = 400, error_code = "BE1003", error_message = "invalid email")
        
        user = db.session.query(User).filter(User.email == email).first()

        if user:
            raise BusinessValidationError(status_code = 400, error_code = "BE1006", error_message = "duplicate email")
        
        user = db.session.query(User).filter(User.username == username).first()

        if user is None:
            raise NotFoundError(status_code = 404)
        
        user.email = email
        db.session.add(user)
        db.session.commit()

        return user
        


    def delete(self, username):
        # check if the user exists
        user = db.session.query(User).filter(User.username == username).first()

        if user is None:
            raise NotFoundError(status_code = 404)
        # Check if there are articles for this user, throw exception
        articles = Article.query.filter(Article.authors.any(username = username)).first()
        if articles:
            raise BusinessValidationError(status_code = 400, error_code = "BE1005", error_message = "cant delete users as there are articles written by this user")
        # if no dependency then delete
        db.session.delete(user)
        db.session.commit()
        return "", 200

    @marshal_with(output_fields)
    def post(self):
        args = create_user_parser.parse_args()
        username = args.get("username", None)
        email = args.get("email", None)

        if username is None:
            raise BusinessValidationError(status_code = 400, error_code = "BE1001", error_message = "username is required")
        
        if email is None:
            raise BusinessValidationError(status_code = 400, error_code = "BE1002", error_message = "email is required")
        
        if '@' in email:
            pass
        else:
            raise BusinessValidationError(status_code = 400, error_code = "BE1003", error_message = "invalid email")
        
        user = db.session.query(User).filter((User.username == username) | (User.email == email)).first()

        if user:
            raise BusinessValidationError(status_code = 400, error_code = "BE1004", error_message = "duplicate user")
        
        new_user = User(username= username, email = email)
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201