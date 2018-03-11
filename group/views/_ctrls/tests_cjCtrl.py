#coding=UTF-8

#import os, sys, platform
import copy, re, random
from flask import request, g
from core import dbop, files, urlpy, argv
from _exts import cjfang
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

    def tqAct(self):
        data = {}
        return data

'''

'''
