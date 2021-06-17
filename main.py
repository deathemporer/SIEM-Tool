from flask import Flask, render_template, request
from flask.helpers import url_for
from werkzeug.utils import secure_filename
import json

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/analyse/', methods=['post','get'])
def analyze():
    if request.method == 'POST':
        file = request.files['logfile']
        file.save(secure_filename(file.filename))
        logs = {}
        f = open("logs.txt", 'r')
        lines = f.readlines()
        loglist = []
        for line in lines:
            if len(line.split(' -- ')) != 1:
                logs['timestamp'] = line[:24]
                logs['eventCode'] = line[57:62]
                logs['logType'] = line.split(' -- ')[1]
                logs['message'] = line.split(' -- ')[2].rsplit(',  \n')[0]
                loglist.append(logs.copy())
            else:
                continue
        jsonString = json.dumps(loglist)
        jsonFile = open("log.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        return render_template('log.html', logs = loglist)




if __name__ == '__main__':
    app.run()
