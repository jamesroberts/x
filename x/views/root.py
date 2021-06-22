from flask import Blueprint

root = Blueprint("root", __name__)

counter = 1


@root.route("/")
def test():
    global counter
    counter += 1
    return str(counter)
