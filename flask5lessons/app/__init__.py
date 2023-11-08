from flask import Flask
import os, binascii
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = binascii.hexlify(os.urandom(24))
print(app.config['SECRET_KEY'])
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

from models import User, Session

@login_manager.user_loader
def load_user(user_id: int):
    session = Session()
    return session.query(User).where(User.id == user_id).first()

import routes