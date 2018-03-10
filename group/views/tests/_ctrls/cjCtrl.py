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
        data['_end'] = 1
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
                data['_pend'] = i+1
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
        return data

    def tqAct(self):
        data = {}
        return data

'''

'''
