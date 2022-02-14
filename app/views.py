import os

from flask import render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

import app.service as service
import config
from yolo.detect import run


def upload_callback():
    return redirect('asdfsa')


def home(some_text=None):
    return render_template("index.html", some_text=some_text)


def upload():
    return render_template("test.html")

    # if "file" not in request.files:
    #     return request.files
    #
    # file = request.files["file"]
    #
    # if file.filename == "":
    #     flash("No selected file")
    #     return "bad request", 400

    # return redirect(url_for('download_file', name=filename))

    # if file and service.allowed_file(file.filename):
    #     filename = secure_filename(file.filename)
    #     dirname = os.getcwd() + config.UPLOAD_FOLDER
    #     file.save(os.path.join(dirname, filename))
    #
    #
    #     # TODO: callback
    #     run(callback=upload_callback)


        # return redirect(url_for('download_file', name=filename))

    return "error", 500


def download_file(name):
    return send_from_directory(os.getcwd() + config.UPLOAD_FOLDER, name)
