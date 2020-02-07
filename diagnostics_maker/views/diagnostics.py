from flask import Blueprint
from flask import render_template

mod = Blueprint("diagnostics", __name__, url_prefix="/diagnostics")

@mod.route("/")
def index():
    return render_template("diagnostics.html")