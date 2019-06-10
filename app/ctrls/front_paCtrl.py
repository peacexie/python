#coding=UTF-8

import copy, re
from core import argv, dbop, files, urlpy
from libs import cjfang
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

    # `link`方法
    def linkAct(self):
        durl = 'http://txmao.txjia.com/dev.php'
        xurl = argv.get('url', durl)
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

    # `diy`方法
    def diyAct(self):
        s1st = argv.get('s1st', 'ul')
        s2nd = argv.get('s2nd', 'li')
        satt = argv.get('satt', '') # html(),text(),href,title,width,
        durl = 'http://txmao.txjia.com/dev.php'
        xurl = argv.get('url', durl);
        html = self.rhtml(xurl)
        doc = pyq(html)
        parts = doc(s1st) # div
        res = {}; no = 0; 
        for part in parts:
            # one-part
            itms = pyq(part).find(s2nd)
            if not itms:
                continue
            sres = []
            for itm in itms:
                if satt=='html()':
                    val = pyq(itm).html()
                elif satt=='text()':
                    val = pyq(itm).text()
                elif len(satt)>0:
                    val = pyq(itm).attr(satt)
                else:
                    val = pyq(itm).html()
                if val and '<img' in val:
                    reg = r'src=[\'\"]?([^\'\"]+\.(jpg|gif|png))[\'\"]?'
                    pics = re.findall(reg, val, re.S|re.M)
                    val = '<img width=120 src="'+pics[0][0]+'" />' if pics else '';
                if val:
                    sres.append(val)
                    #print(val);
            # end-part
            no += 1
            res['part'+str(no)] = sres
        data = {'res':res, 'url':xurl, 's1st':s1st, 's2nd':s2nd, 'satt':satt}
        return data

    def rhtml(self, url, scet='', cache=6):
        #cache = 0.0001
        fp = g.dir['cache'] + '/pages/' + files.autnm(url, 1)
        ok = files.tmok(fp, cache)
        if ok:
            html = files.get(fp, 'utf-8')
            html = files.get(fp)
        else:
            html = urlpy.page(url)
            files.put(fp, html)
        return html
        #

'''

'''
