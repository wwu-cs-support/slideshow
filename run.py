import os
import json
from werkzeug import secure_filename
from flask import (Flask, Response, render_template, request, redirect,
        url_for, send_from_directory)

app = Flask(__name__)

app_dir = os.path.join(os.path.dirname(__file__))

app.config['UPLOAD_METADATA'] = os.path.join(app_dir, 'static/metadata.json')
app.config['UPLOAD_FOLDER'] = os.path.join(app_dir, 'static/pictures')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'tiff', 'tif', 'GIF', 'gif', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/upload", methods=['POST', 'GET'])
def upload_picture():
    if request.method == 'POST':
        duration = 5000
        order = 1
        pic=request.files['file']
        duration=int(request.form['duration'])
        order=request.form['order']

        if pic and allowed_file(pic.filename):
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            entry = {}
            entry['path'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            entry['duration'] = duration

            with open(app.config['UPLOAD_METADATA'], 'r+') as json_file:
                metadata = json.load(json_file)
                json_file.seek(0)
                if order != "last":
                    metadata['pictures'].insert((int(order)-1), entry)
                else:
                    metadata['pictures'].insert(len(metadata['pictures']), entry)
                json.dump(metadata, json_file, indent=2)

            return render_template('success.html', filename=filename)
        else:
            return render_template('extension_error.html', extensions=app.config['ALLOWED_EXTENSIONS'])
    else:
        return render_template('upload.html')

@app.route('/static/pictures/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route("/")
def slideshow():
    return render_template('displaypic.html')

@app.route("/pictures")
def pictures():
    with open(app.config['UPLOAD_METADATA'], 'r') as mf:
        return Response(mf.read(), mimetype='application/json')


if __name__ == '__main__':
    debug = True if os.environ.get('SLIDESHOW_DEBUG') else False
    app.run(debug=debug)
