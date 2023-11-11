from flask_restful import Resource
from application.database import db
from application.models import User

class UserAPI(Resource):
    def get(self, username):
        # get the username
        print('In UserAPI GET Method', username)
        # get the user from database based on username
        user = db.session.query(User).filter(User.username == username).first()

        if user:
            # return a valid user json
            return {"user_id": user.user_id, "username" : user.username, "email" : user.email}
        else:
            # return 404 error
            return " ", 404
        # format the return json

        # return
        return {"username" : username, "action" : "GET"}

    def put(self, username):
        print("PUT username", username)
        return {"username" : username, "action" : "PUT"}

    def delete(self, username):
        print("DELETE username", username)
        return {"username" : username, "action" : "DELETE"}

    def post(self):
        print("POST username")
        return {"action" : "POST"}