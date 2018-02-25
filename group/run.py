#coding=UTF-8
#https://stackoverflow.com/questions/7974771/flask-blueprint-template-folder

import sys, io
sys.path.append("../")
from core import vop
from flask import Flask

app = Flask(__name__, template_folder='views')

vop.vrun(app)
#print(app.url_map)
app.run()

'''
db, static, url, dir

'''

