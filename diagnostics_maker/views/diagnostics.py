from flask import (
    Blueprint, render_template, request)
from wtforms import (
    Form, StringField, TextField, TextAreaField, validators 
)
from diagnostics_maker.control.db_accessor import DbAccessor, Diagnostic

mod = Blueprint("diagnostics", __name__, url_prefix="/diagnostics")

@mod.route("/<id>")
def index(id = None):
    # DBから診断情報を取得
    db = DbAccessor()
    diag = db.session.query(Diagnostic).get(id)

    form = MakeDiagnosticsForm(request.form)
    return render_template("diagnostics.html", form=form, diag=diag, id=id)

# 名前入力フォーム
class MakeDiagnosticsForm(Form) :
    name = TextField("username", validators=[
        validators.Required(message="名前を入力してください")
    ])
