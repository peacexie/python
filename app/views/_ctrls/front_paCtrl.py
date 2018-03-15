#coding=UTF-8

import copy, re
from core import argv, dbop, files, urlpy
from _exts import cjfang
from urllib import parse
from flask import request, g
from pyquery import PyQuery as pyq

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    def picAct(self):
        wd = argv.get('wd')
        if len(wd)==0:
            wd = '绿色风景'
        swd = parse.quote(wd)
        urlb = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='
        url = urlb + swd
        html = self.rhtml(url)
        reg = r'"thumbURL"\:"([^\"]+)"'
        itms = re.findall(reg, html, re.S|re.M)
        data = {'res':itms, 'wd':wd}
        return data

    def nipAct(self):
        url = 'http://www.weather.com.cn/html/weather/101281601.shtml'
        html = self.rhtml(url)
        doc = pyq(html)
        lis = doc('.greatEvent li')
        itms = []
        for li in lis:
            link = pyq(li).find('a').attr('href')
            img = pyq(li).find('img').attr('src')
            title = pyq(li).find('h2').text()
            if not img:
                continue
            itms.append({'img':img, 'link':link, 'title':title})
        return itms

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
        durl = 'http://txmao.txjia.com/dev.php'
        xurl = argv.get('url', durl);
        html = self.rhtml(xurl)
        doc = pyq(html)
        itms = doc('a')
        res = []
        for itm in itms:
            url = pyq(itm).attr('href')
            url = urlpy.fxurl(url, durl)
            title = pyq(itm).text()
            res.append({'url':url, 'title':title})
        data = {'res':res, 'url':xurl}
        return data

    def rhtml(self, url, scet='utf-8', cache=6):
        #cache = 0.0001
        fp = g.dir['cache'] + '/pages/' + files.autnm(url, 1)
        ok = files.tmok(fp, cache)
        if ok:
            html = files.get(fp, 'utf-8')
            html = files.get(fp)
        else:
            html = urlpy.page(url, scet)
            files.put(fp, html)
        return html
        #

'''

'''
