from flask import Blueprint

mod = Blueprint("make", __name__, url_prefix="/make")

@mod.route("/")
def index():
    return "Hello. This page is make."