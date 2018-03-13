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

    def picAct(self):
        # https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%B8%85%E6%96%B0%E6%97%A9%E6%99%A8
        # {"thumbURL":"https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3808464009,1726760794&fm=200&gp=0.jpg",
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%B8%85%E6%96%B0%E6%97%A9%E6%99%A8'
        html = self.rhtml(url)
        reg = r'"thumbURL"\:"([^\"]+)"'
        itms = re.findall(reg, html, re.S|re.M)
        return itms

    def nipAct(self):
        url = 'http://www.nipic.com/photo/jingguan/shanshui/index.html'
        html = self.rhtml(url)
        doc = pyq(html)
        lis = doc('.works-box')
        itms = []
        for li in lis:
            link = pyq(li).find('a').attr('href')
            img = pyq(li).find('img').attr('src')
            if not img:
                continue
            itms.append({'img':img, 'link':link})
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
        #url = 'https://www.baidu.com/s?wd=urlopen%20python3&rsv_spt=1&rsv_iqid=0x855eace20002ad5d&issp=1&f=3&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=100&rsv_t=5f47pBEd2r7%2Fe2UPeNQ4YRmL4JOzfn7cLmMYNqfHJXwMmpNzxJVa7TLJNifj92HT1t0k&rsv_sug2=1&prefixsug=urlopen&rsp=0&inputT=1665&rsv_sug4=1665'
        url = 'https://www.baidu.com/s?wd=%E7%88%AC%E8%99%AB&tn=monline_dg&ie=utf-8'
        # u'https://www.baidu.com/baidu?wd='+quote(keyword)+'&tn=monline_dg&ie=utf-8'
        # 爬虫=%E7%88%AC%E8%99%AB

        html = self.rhtml(url)
        doc = pyq(html) # url=r''+url
        divs = doc('.c-container') # h3,.c-container
        #print(pyq(divs).text())
        itms = []
        for itm in divs:
            #print(itm)
            #itm = pyq(itm0).('.result c-container')
            link = pyq(itm).find('h3').find('a')
            url = pyq(link).attr('href')
            title = pyq(link).text()
            rem = pyq(itm).find('.c-abstract').text()
            itms.append({'url':url, 'title':title, 'rem':rem})
        return itms

    def indexAct(self):
        data = {}
        return data

    def rhtml(self, url, cache=6):
        cache = 0.0001
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
