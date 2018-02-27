
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
        # imcat
        db1 = dbop.dbm()
        data['catalog'] = db1.get("SELECT * FROM {base_catalog} WHERE model=%s", ('demo',), 1)
        # blog
        cdb = copy.deepcopy(g.cdb)
        cdb['type'] = 'sqlite3'
        cdb['name'] = g.blog['file']
        db2 = dbop.dbm(cdb)
        data['blog'] = db2.get('SELECT title,text FROM entries ORDER BY id DESC', (), 3)
        # 
        data['d'] = {} #{'tpname':'json'} # 指定模板
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
