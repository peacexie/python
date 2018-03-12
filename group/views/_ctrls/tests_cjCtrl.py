#coding=UTF-8

import copy
from core import argv, dbop, mproc
from _exts import cjfang
from flask import g

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        cdb = dict(copy.deepcopy(g.cdb), **g.cjdb)
        self.db = dbop.dbm(cdb)

    # `attr`方法
    def attrAct(self):
        data = {}
        act = argv.get('act', 'view')
        res = cjfang.area(self.db, act)
        data['res'] = res
        data['_end'] = 1
        return data

    def urlAct(self):
        print('\n\n')
        mp = mproc.Pools(3)
        res = mp.start('p1')
        #
        act = argv.get('act', 'view')
        data = cjfang.url(self.db, act)
        return data

    def dataAct(self):
        act = argv.get('act', 'view')
        data = cjfang.data(self.db, act)
        return data

    def imgAct(self):
        act = argv.get('act', 'view')
        data = cjfang.img(self.db, act)
        return data

    def indexAct(self):
        data = {}
        return data

    def tqAct(self):
        data = {}
        return data

'''

'''
