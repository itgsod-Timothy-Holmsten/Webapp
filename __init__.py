from flask import Flask
#from flask_login import LoginManager

#init the flask app
app = Flask(__name__)

app.secret_key = "troleolol"
#login_manager = LoginManager()
#login_manager.init_app(app)

preloaded_db = "formulas_db.json"

import models
from webapp.views import home, add_formula, search