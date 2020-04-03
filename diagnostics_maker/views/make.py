from flask import (
    Blueprint, Flask, request, redirect,
    url_for, render_template,
)
from wtforms import (
    Form, StringField, TextField, TextAreaField, validators 
)
from ..control.db_accessor import DbAccessor, Diagnostic

mod = Blueprint("make", __name__, url_prefix="/make")

@mod.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")

@mod.route("/create", methods=["GET", "POST"])
def make_diag():
    form = MakeForm(request.form)

    # if form.validate_on_submit():
    if form.validate():
        # db = DbAccessor()
        # diag = Diagnostic()
        # form.populate_obj(diag)
        
        # diag.title = "hoge"
        # diag.baseText = "hogehoge"

        # db.session.add(diag)
        # db.session.commit()

        return redirect(url_for("home.index"))

    return render_template("make.html", form=form)

class MakeForm(Form) :
    title = TextField("診断タイトル*", validators=[
        validators.Required(message="診断タイトルを入力してください")
    ])

    baseText = TextAreaField("診断結果基本テキスト*", validators=[
        validators.Required(message="診断結果基本テキストを入力してください")
    ])

