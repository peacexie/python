#coding=UTF-8

import copy, re
from core import argv, dbop, files, urlpy
from flask import request, g, flash, session

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
            #session['logged'] = False
            g.ses['logged'] = ''
            flash('You were logged out!')
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
        # login
        msg = 'Please login!' if not g.ses['logged'] else 'Your are logged!'
        if request.method == 'POST':
            if request.form['user'] != g.exdb['user']:
                msg = 'Invalid username'
            elif request.form['pass'] != g.exdb['pass']:
                msg = 'Invalid password'
            else:
                #session['logged'] = True
                g.ses['logged'] = True
                #msg = 'Login OK!'
                flash('You were logged in')
                data['d'] = {'tpname':'dir', 'message':'/front/blog-lists'}
        data['msg'] = msg
        return data

    def listsAct(self): # +<del>
        data = self.data
        act = argv.get('act')
        # check
        if not g.ses['logged']:
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
            return data
        # logout
        if act=="del":
            did = argv.get('id')
            self.db.exe('DELETE FROM {article} WHERE id=?',(did,))
            data['d'] = {'tpname':'dir', 'message':'/front/blog-lists?cid=&page=&kw='}
            return data
        # lists
        cid = argv.get('cid')
        data['cid'] = cid
        sfrom = 'SELECT * FROM {article}'
        where = "cid='"+cid+"'" if cid else '1=1' # 安全???
        data['catalog'] = self.db.get('SELECT * FROM {catalog}')
        data['blog'] = self.db.get(sfrom+' WHERE '+where+' ORDER BY id DESC', (), 20)
        return data

    # `form`方法
    def formAct(self): # add/edit
        data = self.data
        # check
        if not g.ses['logged']:
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
            return data
        # row
        eid = argv.get('id')
        data['data'] = self.db.get(sfrom+' WHERE id=? ORDER BY id DESC', (eid,), 1)
        return data

'''

'''
