#coding=UTF-8

import sys, io
sys.path.append("../")
from core import config, dbop, vop
_cfgs = config.init()
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# all the imports 
from flask import Flask, request, g, render_template #, \
#    redirect, url_for, abort, flash, session


app = Flask(__name__, template_folder='tpls')
config.app(app, _cfgs) # app.config.from_pyfile('./data/cfgapp.py')


@app.before_request
def before_request():
    g.db = dbop.conn(_cfgs)

@app.teardown_request
def teardown_request(exception):
    g.db.close()


''' >用户扩展
@app.route('/exuser/exact')
def exuser(name=''):
    return '/exuser/exact!'
'''
@app.route('/blog/')
def blog_home():
    cur = g.db.execute('SELECT title,text FROM entries ORDER BY id DESC')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('root/blog/lists.htm', entries=entries)


@app.route('/')
@app.route('/<vgp>/')
@app.route('/<mkv>')
@app.route('/<vgp>/<mkv>')
def route(vgp='', mkv=''):
    #print(app.config['PORT'])
    _cfgs['mkvs'] = vop.mkvs(vgp, mkv)
    _vres = {'data':{}, 'vgp':vgp} # data, state, tpname, tpath
    #print(app); print(request); print(g); print(_cfgs)
    _vres = vop.vres(app, request, g, _cfgs)
    return render_template('root/index.htm', _cfgs=_cfgs, _vres=_vres)

if __name__ == '__main__':
    app.run()

