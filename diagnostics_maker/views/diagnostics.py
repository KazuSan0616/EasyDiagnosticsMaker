from flask import Blueprint

mod = Blueprint("diagnostics", __name__, url_prefix="/diagnostics")

@mod.route("/")
def index():
    return "Hello. This page is diagnostics."