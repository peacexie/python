#coding=UTF-8

#import os, sys, platform
import copy, re, random
from flask import request, g
from core import dbop, files, urlpy, req
from _exts import cjfang
from pyquery import PyQuery as pyq
from multiprocessing import Pool, Process

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        #cdb = dict(copy.deepcopy(g.cdb), **g.cjdb)
        #self.db = dbop.dbm(cdb)

    # `attr`方法
    def attrAct(self):
        data = {}
        act = req.get('act', 'view')
        res = cjfang.area(self.db, act)
        data['res'] = res
        data['_end'] = 1
        return data

    def urlAct(self):
        act = req.get('act', 'view')
        data = cjfang.url(self.db, act)
        return data

    def dataAct(self):
        act = req.get('act', 'view')
        data = cjfang.data(self.db, act)
        return data

    def imgAct(self):
        act = req.get('act', 'view')
        data = cjfang.img(self.db, act)
        return data

    def indexAct(self):
        # https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%B8%85%E6%96%B0%E6%97%A9%E6%99%A8
        # {"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3808464009,1726760794&fm=200&gp=0.jpg",
        
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%B8%85%E6%96%B0%E6%97%A9%E6%99%A8'
        html = self.rhtml(url)
        itms = self.hitms(html)

        url = 'http://soso.nipic.com/?q=2018logo'
        itms = self.hitmn(url)

        return itms

    def tqAct(self):
        data = {}
        return data

    def hitmn(self, url, flag=6): # .nipic.com/
        doc = pyq(url=r''+url)
        lis = doc('.new-search-works-item')
        itms = []
        for li in lis:
            url = pyq(li).find('img').attr('data-original')
            if not url:
                continue
            itms.append(url)
        return itms

    def hitms(self, html, flag=6): # .baidu.com/
        reg = r'"thumbURL"\:"([^\"]+)"'
        itms = re.findall(reg, html, re.S|re.M)
        return itms

    def rhtml(self, url, cache=6):

        fp = '.' + g.dir['cache'] + '/pages/' + files.fulnm(url)
        ok = files.tmok(fp, cache)
        if ok:
            html = files.get(fp, 'utf-8')
            html = files.get(fp)
        else:
            html = urlpy.page(url, 'utf-8')
            files.put(fp, html)
        return html
        #

'''

'''
