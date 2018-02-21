#coding=UTF-8
#https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder

import sys, io
sys.path.append("../")
from core import vop
from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

@app.route('/<mkv>')
def route(mkv=''):
    return render_template('root/home/index.htm')

vop.run(app)

#print(app.url_map)
app.run()
