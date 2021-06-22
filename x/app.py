import os
from flask import Flask
from x.views import root


def init_app():
    app = Flask(__name__)
    app.secret_key = os.urandom(32).hex()

    app.register_blueprint(root)

    return app
