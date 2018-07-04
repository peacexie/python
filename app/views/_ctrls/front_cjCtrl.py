#coding=UTF-8

import copy
from core import argv, dbop
from _exts import cjfang, mdo

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        cdb = dict(copy.deepcopy(argv.cfgs['cdb']), **argv.cfgs['cjdb'])
        self.db = dbop.dbm(cdb)

    #fixSale
    def fixSaleAct(self):
        data = {}
        cjfang.fixSale(self.db, 1)
        res = data['res'] = 'res'
        data['_end'] = 1
        return data

    # `attr`方法
    def attrAct(self):
        data = {}
        act = argv.get('act', 'view')
        res = cjfang.area(self.db, act)
        data['res'] = res
        data['_end'] = 1
        return data

    def urlAct(self):
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

    def batchAct(self):
        data = {}
        #print('\nxxxx\n')
        #mp = mdo.Pools('caiji');
        #res = mp.start('area', 'test', 2)
        #data['res'] = res
        return data
        pass

'''

'''
