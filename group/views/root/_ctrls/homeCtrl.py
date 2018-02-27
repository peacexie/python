
#import os, sys, platform
from flask import request, g
from core import dbop

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # imcat, blog

    def indexAct(self):
        data = {}
        #db = dbop.conn(cfgs)
        db = dbop.dbm()
        data['list'] = db.get("SELECT * FROM {base_catalog} WHERE model=%s", ('demo',), 1)

        return data
        
        cur = g.db.execute('SELECT title,text FROM entries ORDER BY id DESC')
        data['list'] = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
        data['d'] = {} #{'tpname':'xml'} # 指定模板
        return data

    # `detail`方法
    def _detailAct(self):
        data = {'_detailAct_msg':'from _detailAct'}
        return data

    # 默认非`detail`方法
    def _defAct(self):
        d = {'tpname':'home/info'} # 指定模板
        #d = {'code':404} # 显示错误访问
        d = {}
        data = {'_defAct_msg':'from _defAct', 'd':d}
        return data 


'''

'''
