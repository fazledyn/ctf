from flask import Blueprint, request, render_template
from application.util import patpat

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@api.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return {'status': 'failed', 'message': 'No file provided'}, 400

    file = request.files['file']
    if file.filename == '':
        return {'status': 'failed', 'message': 'No file selected'}, 400

    return patpat(file)