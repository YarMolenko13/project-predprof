from flask import Flask

import app.views as views
from config import *

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")
app.config["SECRET_KEY"] = SESSION_SECRET
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

app.add_url_rule('/', view_func=views.home)
app.add_url_rule('/api/upload', view_func=views.upload, methods=["POST"])
app.add_url_rule('/download_file/<string:name>', view_func=views.download_file)

if __name__ == "__main__":
    app.run(port=3000)
