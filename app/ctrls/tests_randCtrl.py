
#import os, sys, platform
import copy
from core import argv, dbop, files
from libs import rands
from flask import g

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        #vfmt = argv.get('_vfmt')
        #data = {}
        #if vfmt:
            #data['d'] = {'tpname':vfmt} # 指定模板(格式:xml,json)
        #self.data = data

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    def indexAct(self):
        data = {}
        tp = argv.get('type', '0')
        rn = argv.get('rn', '20') # 10/20
        cm = argv.get('cm', '2')
        ax = argv.get('all', '100')
        s0 = rands.rn(tp, int(ax));
        data['tabs'] = rands.strg(s0, int(rn), int(cm));
        data['argv'] = {'tp':tp, 'rn':rn, 'cm':cm, 'ax':ax};
        #data['pk'] = rands.puke();
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

    # chart
    def chartAct(self):
        data = {}
        tp = argv.get('type', '0')
        rn = argv.get('rn', '20') # 10/20
        cm = argv.get('cm', '2')
        ax = argv.get('all', '100')
        s0 = rands.rn(tp, int(ax));
        data['tabs'] = rands.strg(s0, int(rn), int(cm));
        data['argv'] = {'tp':tp, 'rn':rn, 'cm':cm, 'ax':ax};
        return data

'''

'''
