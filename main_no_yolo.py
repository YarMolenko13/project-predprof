from flask import Flask, render_template

import app.views as views
from config import *

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

def home(some_text=None):
    return render_template("index.html", some_text=some_text)

app.add_url_rule('/', view_func=home)

if __name__ == "__main__":
    app.run(port=3000)
