#coding=UTF-8

#import os, sys, platform
import copy
from flask import request, g
from core import dbop, files, urlpy, req, cjfang
from pyquery import PyQuery as pyq

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
        data = {}
        dmkey = '#newhouse_loupai_list li div.nlc_details'
        itms = cjfang.ritms(g.cjcfg['url'].replace('{page}','1'), dmkey)

        for i in itms:
            itm = {}
            title = pyq(i).find('.nlcd_name').text()
            itm['title'] = title
            itm['url'] = pyq(i).find('a').eq(1).attr('href')
            itm['thumb'] = pyq(i).find('img').attr('src')
            #('img[width="168"]').attr('src')
            #('img').eq(1).attr('src')
            itm['tags'] = pyq(i).find('.fangyuan').text()
            itm['price'] = pyq(i).find('.nhouse_price').text()
            data[title] = itm
            #print(tit)
            #fid = pyq(j).attr('href').replace('/house/s/','').replace('/','')
        pass
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

        '''
        for i in itms:  
            print(pyq(i))
            for j in pyq(i).find('a'):  
                print(pyq(j).attr('href'), pyq(j).text(),)
                pass
        '''

        #doc2 = pyq(url=r'http://txjia.com/tip/')  
        #itms2 = doc2('div.home-b') 

        #data['data2'] = itms2

        #data['xxx'] = {'key1':'val1'}
        return data


'''

'''
