from apps import app
from flask import flash, redirect, render_template, request, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.files)
        
        # check if the post request has the name='image' in html input tag
        if 'image' not in request.files:
            flash('Incorrect name used for input')
            return redirect(request.url)

        image = request.files['image']

        # user enters a blank file
        if image.filename== '': 
            flash('No selected file')
            return redirect(request.url)

        if image and allowed_file(image.filename):
            filename = secure_filename(image.filename)
            
            # grab the base directory leading up to project folder
            basedir = os.path.abspath(os.path.dirname(__file__))
            image.save(os.path.join(basedir, app.config['UPLOAD_FOLDER'], filename))            

            return redirect(url_for('download_file', name=filename))

    return render_template('index.html')

@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config['UPLOAD_FOLDER'], name)