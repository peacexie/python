#coding=UTF-8

import sys
sys.path.append("../")
from core import config
_cfgs = config.init()

from flask import Flask, request, g, render_template, flash

#print(g)
print(_cfgs['envs'])
print(_cfgs['base'])

sys.exit()

#print(start._cfg)

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

from urllib.parse import urlparse
#items = urlparse(url); 
@app.route('/')
def rop():
    return request
    return 'rop:(' + items.path + ')'

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True
    #print(start)
    app.run()


'''
_cfg.root
_cfg.sys
_cfg.ver
vop.run()
vop.group()
vop.show(tpl,data,flag)
    return render_template(tpl+'.html')
'''
