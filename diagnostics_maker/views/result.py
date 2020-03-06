from flask import Blueprint
from diagnostics_maker.control.db_accessor import DbAccessor, Diagnostic

mod = Blueprint("result", __name__, url_prefix="/result")

@mod.route("/")
def index():

    db = DbAccessor()
    diag = Diagnostic()
    #diag.id = 1
    diag.title = "hoge"
    diag.baseText = "hogehoge"

    db.session.add(diag)
    db.session.commit()


    return "Hello. This page is result."

