
#import os, sys, platform
import copy
from flask import g
from core import dbop, files, argv

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
        data['name'] = argv.get('name', 'Python&Flask')

        # sys-db
        data['news'] = g.db.get("SELECT * FROM {docs_news} WHERE did>%s ORDER BY did DESC", ('2015',), 2)
        
        # blog
        cdb1 = dict(copy.deepcopy(g.cdb), **g.exdb)
        db1 = dbop.dbm(cdb1)
        data['blog'] = db1.get('SELECT title,detail FROM {article} ORDER BY id DESC', (), 1)

        # caiji
        cdb2 = dict(copy.deepcopy(g.cdb), **g.cjdb)
        db2 = dbop.dbm(cdb2)
        data['attr'] = db2.get('SELECT * FROM {attr} ORDER BY id DESC', (), 1)

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
        g = argv.get('g', 'root')
        c = argv.get('c', 'homeCtrl')
        a = argv.get('a', 'coderAct')
        tpl = argv.get('tpl', 'root/home/coder.htm')
        fctr = './views/'+g+'/_ctrls/'+c+'.py'
        ftpl = './views/'+tpl
        sctr = files.get(fctr)
        stpl = files.get(ftpl)
        data = {'stpl':stpl, 'sctr':sctr, 'ftpl':ftpl, 'fctr':fctr, 'fact':a}
        return data

    # `link`方法
    def linkAct(self):
        fp = argv.get('fp', 'doc-note.txt')
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
