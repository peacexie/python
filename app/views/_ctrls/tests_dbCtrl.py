
#import os, sys, platform
import copy
from core import argv, dbop, files
from flask import g

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        vfmt = argv.get('_vfmt')
        data = {}
        if vfmt:
            data['d'] = {'tpname':vfmt} # 指定模板(格式:xml,json)
        self.data = data

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    def indexAct(self):
        data = {}
        return data

    # `sqlite`方法# blog
    def sqliteAct(self):
        data = self.data
        cdb1 = dict(copy.deepcopy(g.cdb), **g.exdb)
        db1 = dbop.dbm(cdb1)
        data['blog'] = db1.get('SELECT * FROM {article} ORDER BY id DESC', (), 20)
        data['catalog'] = db1.get('SELECT * FROM {catalog}')
        #data['d'] = {'tpname':'json'}
        return data

    # `mysql`方法
    def mysqlAct(self):
        data = self.data
        data['news'] = g.db.get("SELECT * FROM {docs_news} WHERE did>%s ORDER BY did DESC", ('2015',), 20)
        return data

    # 默认非`both`方法
    def bothAct(self):
        data = {}
        # news
        data['news'] = g.db.get("SELECT * FROM {docs_news} WHERE did>%s ORDER BY did DESC", ('2015',), 3)
        # blog
        cdb1 = dict(copy.deepcopy(g.cdb), **g.exdb)
        db1 = dbop.dbm(cdb1)
        data['blog'] = db1.get('SELECT * FROM {article} ORDER BY id DESC', (), 3)
        return data

'''

'''
