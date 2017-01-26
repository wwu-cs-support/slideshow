import os
import json
from werkzeug import secure_filename
from flask import (Flask, Response, render_template, request, redirect,
        url_for, send_from_directory)

app = Flask(__name__)

app_dir = os.path.join(os.path.dirname(__file__))

app.config['UPLOAD_METADATA'] = os.path.join(app_dir, 'static/metadata.json')
app.config['UPLOAD_FOLDER'] = os.path.join(app_dir, 'static/pictures')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'tiff', 'tif', 'gif', 'mov'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route("/delete", methods=['POST', 'GET'])
def delete_picture():
    if request.method == 'GET':
        return render_template('delete.html')
    else:
        pic=request.form.get('filename')
        filename = os.path.join(app.config['UPLOAD_FOLDER'], pic)
        metadata = json.load(open(app.config['UPLOAD_METADATA']))

        for item in metadata['pictures']:
            if item['path'] == filename:
                metadata['pictures'].remove(item)
        with open(app.config['UPLOAD_METADATA'], 'w') as json_file:
            json.dump(metadata, json_file, indent=2)

        return render_template('success.html', message="deleted {} from ".format(pic))

@app.route("/upload", methods=['POST', 'GET'])
def upload_picture():
    if request.method == 'POST':
        duration = 5000
        order = 1
        pic=request.files['file']
        if request.form.get('duration'):
            duration=int(request.form.get('duration'))*1000
        order=int(request.form.get('order') or 1)

        if pic and allowed_file(pic.filename.lower()):
            filename = secure_filename(pic.filename)
            pic.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            entry = {}
            entry['path'] = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            entry['duration'] = duration

            with open(app.config['UPLOAD_METADATA'], 'r+') as json_file:
                metadata = json.load(json_file)
                json_file.seek(0)
                metadata['pictures'].insert((int(order)-1), entry)
                json.dump(metadata, json_file, indent=2)

            return render_template('success.html', message="uploaded {} to ".format(filename))
        else:
            return render_template('extension_error.html', extensions=app.config['ALLOWED_EXTENSIONS'])
    else:
        return render_template('upload.html')

@app.route('/reorder', methods=['POST', 'GET'])
def reorder_picture():
    if request.method == 'POST':
        return render_template('success.html', message="changed the order of ")
    else:
        with open(app.config['UPLOAD_METADATA'], 'r+') as json_file:
            metadata = json.load(json_file)

        pic_array = [metadata['pictures'][i]['path'] for i in range(len(metadata['pictures']))]

        return render_template('reorder.html', pic_array=pic_array)

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
    if (not os.path.isfile(app.config['UPLOAD_METADATA']) or os.stat(app.config['UPLOAD_METADATA']).st_size==0):
        json_string = '{"pictures": []}'
        with open(app.config['UPLOAD_METADATA'], 'w') as json_file:
            json_file.write(json_string)

    app.run(debug=debug)
