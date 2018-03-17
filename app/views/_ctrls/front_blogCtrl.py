#coding=UTF-8

import copy
from core import argv, dbop
from flask import request, g, flash, session

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        cdb = dict(copy.deepcopy(g.cdb), **g.exdb)
        self.db = dbop.dbm(cdb)
        self.data['catalog'] = self.db.get('SELECT * FROM {catalog}')
        cdic = {}
        for itm in self.data['catalog']:
            cdic[itm['kid']] = itm['title']
        self.data['cdic'] = cdic

    def indexAct(self):
        data = self.data
        parts = {}
        for itm in data['catalog']:
            sql = 'SELECT * FROM {article} WHERE cid=? ORDER BY id DESC'
            blogs = self.db.get(sql, (itm['kid'],), 5)
            if blogs:
                parts[itm['kid']] = blogs
        data['parts'] = parts
        return data

    def _mtypeAct(self):
        data = self.data
        sql = 'SELECT * FROM {article} WHERE cid=? ORDER BY id DESC'
        data['blog'] = self.db.get(sql, (g.mkvs['key'],), 20)
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
            return data
        # login
        msg = 'Please login!' if not g.ses['logged'] else 'Your are logged!'
        if request.method == 'POST':
            if request.form['user'] != g.exdb['user']:
                msg = 'Invalid username'
            elif request.form['pass'] != g.exdb['pass']:
                msg = 'Invalid password'
            else:
                #session['logged'] = True
                g.ses['logged'] = 1
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
        if act=="del": # ?cid=&page=&kw=
            oid = argv.get('id')
            self.db.exe('DELETE FROM {article} WHERE id=?',(oid,))
            data['d'] = {'tpname':'dir', 'message':'/front/blog-lists'}
            return data
        # lists
        cid = argv.get('cid')
        data['cid'] = cid
        where = "cid='"+cid+"'" if cid else '1=1' # 安全???
        sql = 'SELECT * FROM {article} WHERE '+where+' ORDER BY id DESC'
        data['blog'] = self.db.get(sql, (), 20)
        return data

    # `form`方法
    def formAct(self): # add/edit
        data = self.data
        # check
        if not g.ses['logged']:
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
            return data
            #pass
        # post
        data['id'] = oid = argv.get('id')
        if request.method == 'POST':
            title = request.form['title']
            cid = request.form['cid']
            detail = request.form['detail']
            if oid:
                sql = 'UPDATE {article} SET title=?,cid=?,detail=? WHERE id=?'
                sp = (title, cid, detail, oid)
            else:
                sql = 'INSERT INTO {article} (title,cid,detail) values (?,?,?)'
                sp = (title, cid, detail)
            self.db.exe(sql, sp)
            flash('Article posted ok!')
            data['d'] = {'tpname':'dir', 'message':'/front/blog-lists'}
            return data
        # row
        data['row'] = self.db.get('SELECT * FROM {article} WHERE id=?', (oid,), 1)
        if not data['row']:
            data['id'] = oid = ''
        data['r_cid'] = data['row']['cid'] if data['row'] else ''
        data['msg'] = '修改:id='+str(oid) if oid else '增加'
        return data

    # `_detail`方法
    def _detailAct(self): # detail
        data = self.data
        data['id'] = oid = g.mkvs['key']
        # row
        data['row'] = self.db.get('SELECT * FROM {article} WHERE id=?', (oid,), 1)
        if not data['row']:
            data['d'] = {'tpname':'dir', 'message':'/front/blog'}
            return data
        data['row']['detail'] = data['row']['detail'].replace('\n', '<br>\n').replace(' ', '&nbsp;')
        return data

'''

'''
