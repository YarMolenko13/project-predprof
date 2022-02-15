import os
import uuid

from flask import render_template, request, flash, redirect, send_from_directory, session
from werkzeug.utils import secure_filename

import app.service as service
from config import *
from main_no_yolo import SESSION_USER


# from yolo.detect import run


def upload_callback():
    return redirect('asdfsa')


def home(some_text=None):
    user_id = uuid.uuid1()
    session[SESSION_USER] = user_id

    # TODO: change path
    print("make dirs")

    root_path = "\\".join(os.getcwd().split("\\"))
    root_path = root_path.replace("\\", "/")

    os.makedirs(f"{root_path}{UPLOAD_FOLDER}/{str(user_id)}/input")
    os.makedirs(f"{root_path}{UPLOAD_FOLDER}/{str(user_id)}/output")

    return render_template("index.html", some_text=some_text)


# TODO: try catch
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

        root_path = "\\".join(os.getcwd().split("\\")[0:-1])
        dirname = f'{root_path}{UPLOAD_FOLDER}/{str(user_id)}/input'

        path = os.path.join(dirname, filename)
        path = path.replace("\\", "/")

        file.save(path)

    return "good", 200


def download_file(name):
    return send_from_directory(os.getcwd() + UPLOAD_FOLDER, name)
