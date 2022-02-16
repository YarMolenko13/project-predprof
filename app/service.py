import os
import shutil

from config import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, INPUT_FOLDER


def allowed_file(filename: str):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def get_user_path(user_id):
    root_path = "\\".join(os.getcwd().split("\\"))
    user_path = f"{root_path}{UPLOAD_FOLDER}/{user_id}"
    user_path = user_path.replace("\\", "/")

    return user_path


def clear_user_input_folder(user_id):
    try:
        input_path = (get_user_path(user_id) + INPUT_FOLDER).replace("\\", "/")

        if os.path.exists(input_path):
            shutil.rmtree(input_path)

            os.makedirs(input_path)
    except Exception as e:
        print(e)

def create_user_folder_and_get_path(user_id):
    try:
        user_path = get_user_path(user_id)

        if not os.path.exists(user_path):
            print("make dirs")

            os.makedirs(f"{user_path}/input")
            os.makedirs(f"{user_path}/output")

    except Exception as e:
        print(e)
