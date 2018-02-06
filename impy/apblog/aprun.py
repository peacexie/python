#coding=UTF-8

import sys
sys.path.append("../")
from core import config, dbop, vop
_cfgs = config.init()

#import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# all the imports // , json

from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# configuration
DATABASE = './flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'


app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = dbop.conn(_cfgs['base']['db']) #connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

''' >用户扩展
@app.route('/exuser/exact')
def exuser(name=''):
    return '/exuser/exact!'
'''
@app.route('/blog/')
def lists():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('blog/lists.htm', entries=entries)


@app.route('/')
@app.route('/<vgp>/')
@app.route('/<mkv>')
@app.route('/<vgp>/<mkv>')
def rop(vgp='', mkv=''):

    _cfgs['mkvs'] = vop.mkvs(vgp, mkv)
    res = {'data':{}, 'vgp':vgp} # data,mkvs,vgp,mkv,
    g.res = res 
    tpname = vop.tpname(_cfgs)
    return render_template('root/index.htm', res=res)

if __name__ == '__main__':
    app.run()


