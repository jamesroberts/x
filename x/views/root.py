from flask import Blueprint

root = Blueprint("root", __name__)


@root.route("/")
def test():
    return 'test'
