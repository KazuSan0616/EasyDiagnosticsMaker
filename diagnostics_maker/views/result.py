from flask import (
    Blueprint, render_template, request)
from diagnostics_maker.control.db_accessor import DbAccessor, Diagnostic, DiagnosticsList
import datetime

mod = Blueprint("result", __name__, url_prefix="/result")

@mod.route("/<id>", methods=["POST"])
def index(id = None):
    # POSTデータを取得
    name = request.form["name"]

    # DBから診断情報を取得
    db = DbAccessor()
    diag = db.session.query(Diagnostic).get(id)
    itemList = db.session.query(DiagnosticsList).filter(DiagnosticsList.diagId == id)
    
    # 表示テキストを作成
    text = generateDiagResult(diag.baseText, name, itemList)

    return render_template("result.html", title=diag.title, baseText=text)

#名前と日付から本日の値を取得する
def createTodayValueFromName(name):
    now = datetime.datetime.now()
    todayValue = now.year * 10000 + now.month * 100 + now.day
    nameValue = 0
    for char in name:
        nameValue += ord(char)
    return todayValue + nameValue

#表示テキスト作成処理
def generateDiagResult(baseText, name, itemList):
    lIdx = createTodayValueFromName(name) % itemList.count()
    genText = baseText.replace("[USER]", name).replace("[LIST]", itemList[lIdx].listItem)
    
    return genText