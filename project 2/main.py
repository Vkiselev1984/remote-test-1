from flask import Flask
from backend.controller import UserController
import json

app = Flask(__name__, template_folder='frontend')

with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

UserController(app, config)

if __name__ == '__main__':
    app.run(debug=True)