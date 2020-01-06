from flask import Blueprint

mod = Blueprint("home", __name__, url_prefix="/")

@mod.route("/")
def index():
    return "Hello. This page is home."

