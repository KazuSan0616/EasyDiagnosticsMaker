from flask import Flask
from .views import home
from .views import make
from .views import diagnostics
from .views import result

app = Flask(__name__)
app.register_blueprint(home.mod)
app.register_blueprint(make.mod)
app.register_blueprint(diagnostics.mod)
app.register_blueprint(result.mod)
