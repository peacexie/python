#coding=UTF-8

import sys
#import io
sys.path.append("../")
sys.path.append("../import")
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# all the imports // , json
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from contextlib import closing
from core import config as _cfg

# configuration
DATABASE = './flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = '123456'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        #with app.open_resource('./schema.sql') as f:
        #    db.cursor().executescript(f.read()) 
        # ValueError: script argument must be unicode.
        db.cursor().executescript(dbsql)
        db.commit()

'''
dbsql = '\
drop table if exists entries;\
create table entries (\
  id integer primary key autoincrement,\
  title string not null,\
  text string not null\
);\
'''

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)


@app.before_request
def before_request():
    g.db = connect_db()

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
@app.route('/<tpl>/')
@app.route('/<mkv>')
@app.route('/<tpl>/<mkv>')
def rop(tpl='', mkv=''):
    if len(mkv)==0:
        type = 'mhome'
        mkv = 'home-index'
    elif mkv.find('.')>0:
        type = 'detail'
    elif mkv.find('-')>0:
        type = 'mtype'
    else:
        type = 'mhome'
        mkv = mkv + '-index'
    tmp = mkv.split('.') if mkv.find('.')>0 else mkv.split('-')
    view = tmp[2] if len(tmp)>=3 else ''
    mkvs = {'tpl':tpl, 'mkv':mkv, 'type':type, 'mod':tmp[0], 'key':tmp[1], 'view':view}
    g.mkvs = mkvs
    res = {'data':{}, 'tpl':tpl, 'mkv':mkv} # data,mkvs,tpl,mkv,
    g.res = res 
    return render_template('root/index.htm', res=res)

if __name__ == '__main__':
    app.run()


