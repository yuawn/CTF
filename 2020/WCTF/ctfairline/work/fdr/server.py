#!/usr/bin/env python3
from flask import Flask, request
import datetime
app = Flask(__name__)

@app.route('/fdr', methods=['POST'])
def f():
    fi = request.files['fdr-log']
    fi.save('./' + fi.filename)
    return 'Done'

app.run('0.0.0.0', 80, threaded=True)
