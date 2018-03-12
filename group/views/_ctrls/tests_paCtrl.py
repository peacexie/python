#coding=UTF-8

import copy, re
from core import dbop, files, urlpy, argv
from _exts import cjfang
from flask import request, g
from pyquery import PyQuery as pyq

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        #cdb = dict(copy.deepcopy(g.cdb), **g.cjdb)
        #self.db = dbop.dbm(cdb)

    # `diy`方法
    def diyAct(self):
        url = 'http://txmao.txjia.com/dev/start.htm'
        dmkey = '.mod-section'
        key1 = 'li:first'
        key2 = 'ul'
        html = self.rhtml(url)
        doc = pyq(html) # url=r''+url
        itms = doc(dmkey)
        res = {}; no = 0;
        for itm in itms:
            url = itm[0]
            val1 = pyq(itm).find(key1).html()
            val2 = pyq(itm).find(key2).html()
            res['no:'+str(no)] = {'key1['+key1+']':val1, 'key2['+key2+']':val2}
            no += 1
        return res

    # `link`方法
    def linkAct(self):
        data = {}
        return data

    def urlAct(self):
        data = {}
        return data

    def picAct(self):
        data = {}
        return data

    def nipAct(self):
        data = {}
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

        fp = g.dir['cache'] + '/pages/' + files.fulnm(url)
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
