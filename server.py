from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.utils import secure_filename
import os

from har import is_allowed_file
from model import Harmony

UPLOAD_FOLDER = os.getcwd() + '/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Setting maximum allowed payload to 16 megabytes
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
#Required to use Flask sessions, Debug toolbar
app.secret_key = "daksfhausdfskgbxpuseswlduc"


@app.route('/')
def show_home():
    """Display homepage"""

    return render_template("index.html")


@app.route('/donut.json')
def serve_donut_json():
    """Serve data for donut chart"""

    res = session.get('donut', {})

    return jsonify(res)


@app.route('/results')
def show_charts():
    """Display charts of HAR data"""

    return render_template("results.html")


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        print request.files
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect("/")
        harfile = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if harfile.filename == '':
            flash('No selected file')
        if harfile and is_allowed_file(harfile.filename):
            filename = secure_filename(harfile.filename)
            harpath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            harfile.save(harpath)
            print harpath
            print os.listdir(UPLOAD_FOLDER)
            session['har'] = harpath
            current = Harmony(harpath)
            session['donut'] = current.createDoughnut()
            return redirect("/results")

if __name__ == "__main__":
    # Change app.debug to False before launch
    app.debug = True
    app.run(host="0.0.0.0")
