from flask import Blueprint, request

root = Blueprint("root", __name__)


@root.route("/get")
def get():
    return "testing get"


@root.route("/post", methods=['POST'])
def post():
    return "testing post"
