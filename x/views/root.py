from x.shared_cache import SharedCache
from flask import Blueprint
from time import sleep
import random

root = Blueprint("root", __name__)
cache = SharedCache(name="sharedcache")


@root.route("/get")
def get():
    return "testing get"


@root.route("/post", methods=['POST'])
def post():
    return "testing post"


@root.route("/compute")
def compute():
    key = random.randint(0, 10)
    return data(key)


def data(key):
    ret = cache.get(str(key))
    if ret:
        return ret.decode()

    # simulate work
    sleep(0.2)
    cache.set(str(key), "blah")

    return "blah"
