from flask import request
from backend.model import UserModel
from backend.view import UserView
import json

class UserController:
    def __init__(self, app, config):
        self.app = app
        self.model = UserModel(config)
        self.view = UserView()

        @app.route('/')
        def index():
            return self.view.form()

        @app.route('/submit', methods=['POST'])
        def submit():
            user_data = {
                "first_name": request.form['first_name'],
                "last_name": request.form['last_name'],
                "email": request.form['email'],
                "phone": request.form['phone']
            }
            self.model.save_user(user_data)
            return self.view.success()