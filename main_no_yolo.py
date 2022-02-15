import os

from flask import Flask, render_template, request, flash, url_for, send_from_directory
from werkzeug.utils import secure_filename, redirect

import config
from app import service
from config import *

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def home(some_text=None):
    return render_template("index.html", some_text=some_text)


def upload():
    if "file" not in request.files:
        return flash("No selected file")

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return "bad request", 400

    if file and service.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        dirname = os.getcwd() + config.UPLOAD_FOLDER
        file.save(os.path.join(dirname, filename))

    return "error", 500

def results():
    return send_from_directory(os.getcwd() + config.UPLOAD_FOLDER, "30353944.jpg")


app.add_url_rule('/', view_func=home)
app.add_url_rule('/api/upload', view_func=upload, methods=["post"])
app.add_url_rule('/results', view_func=results)

if __name__ == "__main__":
    app.run(port=3000)
