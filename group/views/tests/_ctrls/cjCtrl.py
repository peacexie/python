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
        #cbat = int(g.cjcfg['delimit'])
        proc = int(g.cjcfg['proc'])
        data = {'_end':'-', '_pages':''}
        act = req.get('act', 'view')

        #def tfunc(p, args):
        #    p.apply_async(cjfang.urlp, args=args)

        if act=='done':
            page = int(req.get('page', '1'))
            start = max(cmin, page)
            end = start + proc
            res = {}
            if end>cmax+1:
                end = cmax+1
            #p = Pool(proc);
            for i in range(start, end):
                param = (self.db, act, i)
                cjfang.urlp(self.db, act, i)
                #p.apply_async(tfunc, args=param)
                #p = Process(target=cjfang.urlp, args=param)
                res['_p'+str(i)] = i
            if i>=cmax:
                data['_end'] = 1
            #p.close()
            #p.start()
            #p.join()
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
        #page = req.get('page', '1')
        #if not (act == 'done'):
        #    page = 1 #random.randint(int(g.cjcfg['pagemin']), int(g.cjcfg['pagemax']))
        res = cjfang.datap(self.db, act, 'url')
        data = res #['p'+page]
        return data

    def imgAct(self):
        data = {}
        act = req.get('act', 'view')
        #page = req.get('page', '1')
        #if not (act == 'done'):
        #    page = 1 #random.randint(int(g.cjcfg['pagemin']), int(g.cjcfg['pagemax']))
        res = cjfang.imgp(self.db, act, {})
        data = res #['p'+page]
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


        #  encoding="gb2312"

        # 这个慢死了?
        html = urlpy.page('http://newhouse.jx.fang.com/house/s/', 'gb2312');
        print('urlpy.page:'+html)

        # 这个慢死了?
        html = urlpy.page('http://newhouse.jx.fang.com/house/s/', 'gb2312', {"Accept-Encoding":"gzip"});
        print('urlpy.page:'+html)

        # 这个正常
        #doc = pyq(url=r'https://dg.fang.anjuke.com/loupan/all/')
        #print('anjuke.com:'+doc('title').text())

        # 这个???
        headers = {"User-Agent": "Mozilla/5.0 Window 7 (KHTML, like Gecko) Chrome/31.0", "Accept-Encoding": "gzip"}
        doc = pyq(url=r'http://newhouse.jx.fang.com/house/s/', headers=headers)
        print('fang.com:'+doc('title').text())

        # 这个???
        doc = pyq(url=r'http://au.fang.com/house/')
        print('fang.au:'+doc('title').text())

        # 这个OK
        doc = pyq(url=r'http://www.fang.com/aboutus/index.asp')
        print('fang.about:'+doc('title').text())

        # 这个OK
        #doc = pyq(url=r'http://job.fang.com/index.html')
        #print('fang.job:'+doc('title').text())

        #doc = pyq(url=r'http://dg.fzg360.com/index.php?caid=2&addno=1')
        #print('fzg360.com:'+doc('title').text())

        #itms = doc('div.building_select_table') .encode('utf-8')

        #print('\n==============\n')
        #print(itms)


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
