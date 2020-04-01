from flask import (
    Blueprint, Flask, request, redirect,
    url_for, render_template,
)
from .make import MakeForm
from ..control.db_accessor import DbAccessor, Diagnostic

mod = Blueprint("home", __name__, url_prefix="/")

@mod.route("/")
def index():
    #all_diag = Diagnostic.query.all()
    return render_template("home.html")

@mod.route("/make", methods=["GET", "POST"])
def show_make():
    form = MakeForm(request.form)
    return render_template("make.html", form=form)
