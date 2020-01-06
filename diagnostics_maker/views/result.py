from flask import Blueprint

mod = Blueprint("result", __name__, url_prefix="/result")

@mod.route("/")
def index():
    return "Hello. This page is result."

