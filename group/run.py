#coding=UTF-8

import sys
sys.path.append("../")
from core import vop

from flask import Flask
app = Flask(__name__, template_folder='views')

vop.vrun(app) #print(app.url_map)
app.run()

'''
db, static, url, dir
'''
