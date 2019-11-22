from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/upload/', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
      file = request.files['file']
      if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        a = 'file uploaded'

return render_template('upload.html', data = a)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
