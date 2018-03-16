#coding=UTF-8

import copy, re
from core import argv, dbop, files, urlpy
from _exts import cjfang
from urllib import parse
from flask import request, g, flash, session
from pyquery import PyQuery as pyq

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        cdb = dict(copy.deepcopy(g.cdb), **g.exdb)
        self.db = dbop.dbm(cdb)

    def indexAct(self):
        cid = argv.get('cid')
        sfrom = 'SELECT * FROM {article}'
        data = self.data
        data['catalog'] = self.db.get('SELECT * FROM {catalog}')
        if cid:
            data['blog'] = self.db.get(sfrom+' WHERE cid=? ORDER BY id DESC', (cid,), 20)
        else:
            parts = {}
            for itm in data['catalog']:
                blogs = self.db.get(sfrom+' WHERE cid=? ORDER BY id DESC', (itm['kid'],), 5)
                if blogs:
                    parts[itm['kid']] = blogs
            data['parts'] = parts
        data['cid'] = cid
        cdic = {}
        for itm in data['catalog']:
            cdic[itm['kid']] = itm['title']
        data['cdic'] = cdic
        return data

    def loginAct(self): # +<out>
        data = self.data
        act = argv.get('act')
        # logout
        if act=="out":
            session.pop('logged', None)
            flash('You were logged out!')
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
        # login
        msg = 'Please login!' if not session.get('logged') else 'Your are logged!'
        if request.method == 'POST':
            if request.form['user'] != g.exdb['user']:
                msg = 'Invalid username'
            elif request.form['pass'] != g.exdb['pass']:
                msg = 'Invalid password'
            else:
                session['logged'] = True
                flash('You were logged in')
                data['d'] = {'tpname':'dir', 'message':'/front/lists'}
        data['msg'] = msg
        return data

    def listsAct(self): # +<del>
        data = self.data
        if not session.get('logged'):
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
        return data

    # `form`方法
    def formAct(self): # add/edit
        data = self.data
        return data

'''

from flask import Flask, request, g, render_template, \
    redirect, url_for, abort, flash, session

# create our little application :)
app = Flask(__name__, template_folder='tpls')
config.app(app, _cfgs)

@app.before_request
def before_request():
    g.db = dbop.conn(_cfgs)

@app.teardown_request
def teardown_request(exception):
    g.db.close()


@app.route('/')
def lists():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('blog/lists.htm', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('lists'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != _cfgs['blog']['user']:
            error = 'Invalid username'
        elif request.form['password'] != _cfgs['blog']['pass']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('lists'))
    return render_template('blog/login.htm', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('lists'))

if __name__ == '__main__':
    app.run()

'''
