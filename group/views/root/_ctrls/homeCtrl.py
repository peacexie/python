
#import os, sys, platform
import copy
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
        name = request.args.get('name')
        #/if name:
        data['name'] = name
        # imcat
        db1 = dbop.dbm()
        data['catalog'] = db1.get("SELECT * FROM {base_catalog} WHERE model=%s", ('demo',), 1)
        data['advs'] = g.db.get("SELECT * FROM {base_model} WHERE pid=%s", ('advs',), 2)
        # blog
        cdb = dict(copy.deepcopy(g.cdb), **g.blog)
        db2 = dbop.dbm(cdb)
        data['blog'] = db2.get('SELECT title,detail FROM article ORDER BY id DESC', (), 1)
        # 
        data['d'] = {}
        #data['d'] = {'tpname':'json'} # 指定模板
        #data['d'] = {'tpname':'xml'} # 指定模板

        # 
        #db1.close()
        #db2.close()
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
