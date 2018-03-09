#coding=UTF-8

#import os, sys, platform
import copy, re, random
from flask import request, g
from core import dbop, files, urlpy, req, cjfang
from pyquery import PyQuery as pyq
from multiprocessing import Pool, Process

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
        act = req.get('act', 'view')
        res = cjfang.area(self.db, act)
        data['res'] = res
        return data

    def urlAct(self):
        cmin = int(g.cjcfg['pagemin'])
        cmax = int(g.cjcfg['pagemax'])
        cbat = int(g.cjcfg['delimit'])
        #proc = int(g.cjcfg['proc'])
        data = {'_end':'-', '_pages':''}
        act = req.get('act', 'view')
        if act=='done':
            page = int(req.get('page', '1'))
            start = max(cmin, page)
            end = start + cbat
            if end>cmax+1:
                end = cmax+1
            for i in range(start, end):
                res = cjfang.urlp(self.db, act, i)
                data['_pages'] += str(i) + ','
            if i>=cmax:
                data['_end'] = 1
        else:
            page = random.randint(cmin, cmax)
            res = cjfang.urlp(self.db, act, page)
            data['_pages'] = page
        # 
        data['res'] = res
        return data

    def dataAct(self):
        data = {}
        act = req.get('act', 'view')
        data = cjfang.data(self.db, act)
        return data

    def imgAct(self):
        data = {}
        act = req.get('act', 'view')
        data = cjfang.img(self.db, act)
        return data

    def indexAct(self):
        data = {}

        #cjfang.test()
        #return data

        name = request.args.get('name')
        #/if name:
        data['name'] = name
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

    def tqAct(self):

        data = {}

        return data


'''


        for i in itms:  
            print(pyq(i))
            for j in pyq(i).find('a'):  
                print(pyq(j).attr('href'), pyq(j).text(),)
                pass


        #doc2 = pyq(url=r'http://txjia.com/tip/')  
        #itms2 = doc2('div.home-b') 

        #data['data2'] = itms2

        #data['xxx'] = {'key1':'val1'}

'''
