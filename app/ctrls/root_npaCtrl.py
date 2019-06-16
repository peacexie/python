
#import os, sys, platform
import copy
from core import dbop, files, argv, urlpy
from flask import g
from libs import cjnews, cjtool

# 方法格式: {xxx}Act
# xxx优先顺序 : mkvs.key > mkvs._type > '_def'

# main名称固定
class main:

    # `__init__`一致格式
    def __init__(self, app):
        self.app = app
        self.data = {}
        self.cfgs = argv.init('1')
        self.db = dbop.dbm(self.cfgs['cdb'])
        self.cj = cjnews.main()

    # 规则搜索
    def indexAct(self):
        #url = 'http://txjia.com/'
        #a = urlpy.svurl(url, 'debug')
        parts = {}
        parts['city'] = argv.get('city')
        parts['name'] = argv.get('name')
        parts['rid'] = argv.get('rid')
        rules = self.cj.getRules(parts, 'dict', 1)
        data = {'rules':rules, 'city':parts['city'], 'name':parts['name'], 'rid':parts['rid']}
        return data

    # 爬连接-测试
    def linksAct(self):
        rule = self.getRule()
        if not rule:
            return {'links':{}, 'rule':{}}
        links = self.cj.getUList(rule)
        data = {'links':links, 'rule':rule}
        return data

    # 爬详情-测试
    def detailAct(self):
        rule = self.getRule()
        if not rule:
            return {'detail':{}, 'rule':{}}
        url = argv.get('url')
        title = argv.get('title')
        detail = self.cj.getDetail(rule, url)
        rowb = {'title':title,'url':url}
        skips = cjtool.skips(rule, rowb, detail);
        data = {'detail':detail, 'skips':skips, 'rule':rule, 'rowb':rowb}
        return data

    def getRule(self):
        rid = argv.get('rule')
        sql = "SELECT * FROM {crawl_rule} WHERE id="+rid
        return self.db.get(sql,(),1)

'''

        data['d'] = {}
        #data['d'] = {'tpname':'json'} # 指定模板
        #data['d'] = {'tpname':'xml'} # 指定模板
        #data['d'] = {'tpname':'dir', 'message':'/blog/'} # dir
        #data['d'] = {'code':500, 'message':'500 Message'} # dir

    # 默认非`detail`方法
    def _defAct(self):
        #d = {'tpname':'home/info'} # 指定模板
        #d = {'code':404} # 显示错误访问
        d = {}
        data = {'_defAct_msg':'from _defAct', 'd':d}
        return data 
'''
