#coding=UTF-8

#import os, sys, platform
import copy
from flask import request, g
from core import dbop, files, urlpy
from pyquery import PyQuery as pyq

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}

    # 方法格式: {xxx}Act
    # xxx优先顺序 : mkvs.key > mkvs._type > '_def'
    # exdb, blog

    # `attr`方法
    def attrAct(self):
        data = {}

        # , encoding="gb2312"
        #html = urlpy.page('http://newhouse.jx.fang.com/house/s/', 'gb2312');
        #print(html) 
        #return {'html':html}
        doc = pyq(url=r'http://newhouse.jx.fang.com/house/s/b910/?ctm=1.jx.xf_search.page.9', encoding="gbk")
        
        body = doc('body').text()
        unistr = body.encode('utf-8') 
        utfstr = unistr.decode('utf-8'); print(utfstr)

        print('fang.com:'+doc('body').text())

        #print(doc) #, .decode('gb2312')
        #doc = pyq(doc)  
        #body = doc('body').html() 
        #print(body)
        #print('fang.com:'+body)

        #itms = doc('div.chooseToolBtn')
        #print(itms)

        #page = urllib2.urlopen("http://example")
        #text = unicode(page.read(), "utf-8")

        doc = pyq(url=r'http://dg.fzg360.com/index.php?caid=2&addno=1', encoding="gb2312")  
        print('fzg360.com:'+doc('title').text())
        itms = doc('div.building_select_table')

        print('\n==============\n')
        print(itms)

        for i in itms:  
            print(pyq(i))
            for j in pyq(i).find('a'):  
                print(pyq(j).attr('href'), pyq(j).text(),)
                pass

        #doc2 = pyq(url=r'http://txjia.com/tip/')  
        #itms2 = doc2('div.home-b') 

        #data['data2'] = itms2

        #data['xxx'] = {'key1':'val1'}
        return data

    def indexAct(self):
        data = {}
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


'''

'''
