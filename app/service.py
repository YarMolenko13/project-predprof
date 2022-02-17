import os
import shutil

from config import *


def allowed_file(filename: str):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_user_path(user_id):
    root_path = "\\".join(os.getcwd().split("\\"))
    user_path = f"{root_path}{UPLOAD_FOLDER}/{user_id}"
    user_path = user_path.replace("\\", "/")

    return user_path

def clear_input_folder(user_id):
    try:
        user_path = get_user_path(user_id)
        input_path = user_path + OUTPUT_FOLDER

        if os.path.exists(input_path):
            shutil.rmtree(input_path)

            os.makedirs(input_path)
    except Exception as e:
        print(e)

def clear_input_and_output_folders(user_id):
    try:
        user_path = get_user_path(user_id)

        if os.path.exists(user_path):
            shutil.rmtree(user_path)

            create_user_folder(user_id)
    except Exception as e:
        print(e)

def create_user_folder(user_id):
    try:
        user_path = get_user_path(user_id)

        if not os.path.exists(user_path):
            print("make dirs")

            os.makedirs(user_path + INPUT_FOLDER)
            os.makedirs(user_path + OUTPUT_FOLDER)

    except Exception as e:
        print(e)
