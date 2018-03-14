#coding=UTF-8

import sys, io
sys.path.append("../")
from core import config, dbop, vop
_cfgs = config.init()
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

# all the imports 
from flask import Flask, request, g, render_template, \
    redirect, url_for, abort, flash, session

# create our little application :)
app = Flask(__name__, template_folder='tpls')
config.app(app, _cfgs)
#app.config.from_object(__name__)
#app.config['SECRET_KEY'] = _cfgs['app']['secret_key']
#app.secret_key = _cfgs['app']['secret_key']
#app.config.from_object(_cfgs['app']) # x


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

