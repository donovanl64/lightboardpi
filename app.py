from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/read_file', methods=['GET'])
def read_uploaded_file():
    filename = secure_filename(request.args.get('filename'))
    try:
        if filename and allowed_filename(filename):
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename)) as f:
                for x in f: #until end of file
                    light = f.readline()
                    time = f.readline()

                    makecue(light, time)# Add to cue list?
                    makecue(light, time)

                f.close()

    except IOError:
        pass
    return "Unable to read file"

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
