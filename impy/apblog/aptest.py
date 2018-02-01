#coding=UTF-8

import sys
sys.path.append("../")
sys.path.append("../import")

import scrapy

print(sys.path)

from flask import Flask
from flask import render_template

app = Flask(__name__)
'''
    self,
    import_name,
    static_url_path=None,
    static_folder='static',
    static_host=None,
    host_matching=False,
    template_folder='templates',
    instance_path=None,
    instance_relative_config=False,
    root_path=None
'''

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    app.run()

'''
vop.run()
vop.group()
vop.show(tpl,data,flag)
    return render_template(tpl+'.html')
'''
