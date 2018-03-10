
#import os, sys, platform
import copy
from flask import g
from core import dbop, files, req

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    def indexAct(self):
        data = {}
        data['name'] = req.get('name', 'Python&Flask')
        # blog
        db1 = dbop.dbm()
        data['blog'] = db1.get('SELECT title,detail FROM {article} ORDER BY id DESC', (), 1)
        data['catalog'] = g.db.get("SELECT * FROM {catalog} WHERE kid like? ORDER BY kid DESC", ('%o%',), 2)
        # exdb
        cdb = dict(copy.deepcopy(g.cdb), **g.exdb)
        db2 = dbop.dbm(cdb)
        data['model'] = db2.get("SELECT * FROM {base_model} WHERE pid=%s", ('docs',), 1)
        
        # 
        data['d'] = {}
        #data['d'] = {'tpname':'json'} # 指定模板
        #data['d'] = {'tpname':'xml'} # 指定模板
        #data['d'] = {'tpname':'dir', 'message':'/blog/'} # dir
        #data['d'] = {'code':500, 'message':'500 Message'} # dir

        # 
        db1.close()
        db2.close()
        return data

    # `read`方法
    def readAct(self):
        sread = files.get("../README.md")
        data = {'sread':sread}
        return data

    # `coder`方法
    def coderAct(self):
        g = req.get('g', 'root')
        c = req.get('c', 'homeCtrl')
        a = req.get('a', 'coderAct')
        tpl = req.get('tpl', 'root/home/coder.htm')
        fctr = './views/'+g+'/_ctrls/'+c+'.py'
        ftpl = './views/'+tpl
        sctr = files.get(fctr)
        stpl = files.get(ftpl)
        data = {'stpl':stpl, 'sctr':sctr, 'ftpl':ftpl, 'fctr':fctr, 'fact':a}
        return data

    # `link`方法
    def linkAct(self):
        fp = req.get('fp', 'doc-note.txt')
        slink = files.get("./static/root/doc/"+fp)
        title = '项目计划/开发记录' if fp.find('note')>0 else '学习资料/参考链接'
        data = {'slink':slink, 'fp':fp, 'title':title}
        return data

    # `detail`方法
    def _detailAct(self):
        data = {'_detailAct_msg':'from _detailAct'}
        return data

    # 默认非`detail`方法
    def _defAct(self):
        #d = {'tpname':'home/info'} # 指定模板
        #d = {'code':404} # 显示错误访问
        d = {}
        data = {'_defAct_msg':'from _defAct', 'd':d}
        return data 


'''

'''
