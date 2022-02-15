import os
import shutil
import uuid

from flask import Flask, render_template, request, flash, session
from werkzeug.utils import secure_filename

from app import service
from config import *

SESSION_USER = 'user'

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config["SECRET_KEY"] = SESSION_SECRET
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


def home(some_text=None):
    user_id = uuid.uuid1()
    session[SESSION_USER] = user_id

    # TODO: change path
    print("make dirs")
    os.makedirs(f"{UPLOAD_FOLDER[1:]}/{str(user_id)}/input")
    os.makedirs(f"{UPLOAD_FOLDER[1:]}/{str(user_id)}/output")

    return render_template("index.html", some_text=some_text)


def upload():
    if "file" not in request.files:
        return flash("No selected file")

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return "bad request", 400

    if file and service.allowed_file(file.filename):
        user_id = session[SESSION_USER]
        # TODO : fix filename
        filename = secure_filename(file.filename)

        # TODO: change path
        dirname = f"{os.getcwd()}{UPLOAD_FOLDER}/{str(user_id)}/input"
        path = os.path.join(dirname, filename)
        path = path.replace("\\", "/")

        file.save(path)

    return "error", 500


def results():
    if SESSION_USER in session:
        print("--" * 10, session[SESSION_USER])
        return render_template("results.html", user_id=session[SESSION_USER])

    # return send_from_directory(os.getcwd() + config.UPLOAD_FOLDER, "30353944.jpg")


def delete_folder():
    user_id = session[SESSION_USER]

    dirname = f"{os.getcwd()}{UPLOAD_FOLDER}/{str(user_id)}"
    dirname = dirname.replace("\\", "/")

    shutil.rmtree(dirname)

    return "<h1>deleted</h1>"


app.add_url_rule('/', view_func=home)
app.add_url_rule('/api/upload', view_func=upload, methods=["post"])
app.add_url_rule('/api/delete_folder', view_func=delete_folder, methods=["get"])
app.add_url_rule('/results', view_func=results)

if __name__ == "__main__":
    app.run(port=3000)
