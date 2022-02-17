import os
import uuid

from flask import render_template, request, flash, redirect, session
from werkzeug.utils import secure_filename

import app.service as service
from app.tools import get_results
from config import *


from yolo.detect import run


def upload_callback():
    return redirect('asdfsa')


"""
При заходе на главную страницу, для пользователя создается id и схораняется в session.
Если id уже существует, очищаем папку юзера input (т.к., скорее всего он перешел из results)
"""
def home():
    if SESSION_USER not in session:
        user_id = uuid.uuid1()
        session[SESSION_USER] = str(user_id)
    else:
        print("delete folders home")
        # TODO: delete user folder
        service.clear_input_and_output_folders(session[SESSION_USER])

    return render_template("index.html")


"""
Если в запросе имеется файлы с допустимыми расширениями, создается папка юзера (индивидуальная для каждого пользователя)
с вложенными каталогами input & output
"""
# TODO: try catch
def upload():
    if "file" not in request.files:
        return flash("No selected file")

    file = request.files["file"]

    if file.filename == "":
        flash("No selected file")
        return "bad request", 400

    if file and service.allowed_file(file.filename):
        # TODO: move functional to service
        user_id = session[SESSION_USER]

        service.create_user_folder(user_id)

        user_path = service.get_user_path(user_id)
        input_path = user_path + INPUT_FOLDER
        output_path = user_path + OUTPUT_FOLDER

        filename = secure_filename(file.filename)

        path = os.path.join(input_path, filename)
        path = path.replace("\\", "/")

        file.save(path)
        # спорный вопрос: очищение input перед работой yolo, чтобы нейросеть не обрабатовала те же файлы
        # service.clear_input_folder(user_id)

    return "good", 200


"""
Если session содержит user_id, то рендериться страница с результатом, иначе редирект на главную 
"""
def results():
    if SESSION_USER in session:
        user_id = session[SESSION_USER]

        user_path = service.get_user_path(user_id)
        input_path = user_path + INPUT_FOLDER
        output_path = user_path + OUTPUT_FOLDER

        print(input_path)
        print(output_path)

        # yolo
        # main(source=f"{input_path}", project=f"{output_path}")
        run(source=f"{input_path}", project=f"{output_path}")

        print(get_results(input_path, output_path + '/labels'))

        return render_template("results.html")
    return redirect("/")


"""
Очищение папки input пользователя
"""
# TODO: clear output too
def delete_folder():
    user_id = session[SESSION_USER]

    try:
        service.clear_input_and_output_folders(user_id)
    except Exception as e:
        print(e)
        print("delete error")

        return "deleting user input folder error", 500

    return "good", 200
