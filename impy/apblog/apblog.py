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
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
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


