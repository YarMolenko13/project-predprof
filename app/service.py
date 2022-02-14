from config import ALLOWED_EXTENSIONS

def allowed_file(filename: str):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
