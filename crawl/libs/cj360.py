#coding=UTF-8

import copy, re, time
from core import argv, dbop, files, urlpy
from urllib import parse
from pyquery import PyQuery as pyq
from libs import tools

class main:

    # 构造/析构
    def __init__(self):
        self.cfgs = argv.init('1')
        self.db = dbop.dbm(self.cfgs['cdb'])
    def __del__(self):
        self.db.close(); #print('-end-')

    # 保存一笔详情数据
    def saveDetail(self, rule, rowb):
        kid = str(rowb['id'])
        rowd = self.getDetail(rule, rowb['url'])
        frem = tools.skips(rule, rowb, rowd)
        flag = '1' # '2' if len(frem)>0 else '1'; # 7-待入库/1-爬网址
        ftab = 'flag=%s,frem=%s,ctime=%s, detail=%s,dpub=%s,dfrom=%s, '
        ftab += 'catid=%s,sfrom=%s,suser=%s'
        ctime = time.strftime("%m-%d %H:%M", time.localtime())
        sqli = "UPDATE {crawl_data} SET "+ftab+" WHERE id=%s"
        rowi = (flag,frem,ctime, rowd['detail'],rowd['dpub'],rowd['dfrom'], 
            rule['catid'],rule['sfrom'],rule['suser'], kid)
        res = self.db.exe(sqli,rowi)
        if not frem:
            frem = 'save-ok'
        return 'data-'+kid+' : ' + frem
    # 取出未采集详情的列表
    def getDList(self, part):
        if not part or part=='0':
            whr = '';
        elif part.isdigit():
            whr = " AND ruleid='"+part+"'";
        else:
            whr = " AND city='"+part+"'"
        sql = "SELECT * FROM {crawl_data} WHERE flag=1"+whr
        lists = self.db.get(sql,())
        return lists;

    # 获取规则
    def getRules(self, part):
        if not part or part=='0':
            whr = '';
        elif part.isdigit():
            whr = " AND id='"+part+"'";
        else:
            whr = " AND city='"+part+"'"
        sql = "SELECT * FROM {crawl_rule} WHERE status=1"+whr
        rules = self.db.get(sql,())
        return rules;
    # 爬1个规则的列表
    def pyUrls(self, rule):
        res = {}; no = 0;
        lists = self.getUList(rule)
        for rb in lists:
            url = rb['url']
            sql = "SELECT * FROM {crawl_data} WHERE url=%s"
            odb = self.db.get(sql,(url,),1)
            if not odb:
                fields = 'city,flag,ruleid,title,url'
                sqli = "INSERT INTO {crawl_data} ("+fields+")VALUES(%s,%s,%s,%s,%s)"
                rowi = (rule['city'],'1',rule['id'],rb['title'],rb['url'],)
                rs = self.db.exe(sqli,rowi)
                res[no] = 'save : '+url
            else: # print('skip')
                res[no] = 'skip : '+url
            no += 1;
        #rule = {'id':rule['id'], 'name':rule['name'], 'city':rule['city']}
        return res

    # 采集-获取Url列表
    def getUList(self, rule={}):
        html = self.rhtml(rule['url'])
        doc = pyq(html)
        itms = []
        lists = doc(rule['slist'])
        for li in lists:
            url = tools.pqv(li, rule['surl'], 'href')
            title = tools.pqv(li, rule['stitle'], 'text')
            if not url or not title:
                continue
            url = urlpy.fxurl(url, rule['url'])
            itms.append({'url':url, 'title':title})
        return itms;
    # 采集-获取详情
    def getDetail(self, rule={}, url=''):
        res = {'errno':1, 'errmsg':''}
        html = self.rhtml(url)
        doc = pyq(html)
        detail = tools.pqv(doc, rule['detail'], 'html')
        dpub = tools.pqv(doc, rule['dpub'], 'text')
        dfrom = tools.pqv(doc, rule['dfrom'], 'text')
        return {'dpub':dpub, 'dfrom':dfrom, 'detail':detail}

    # cache: 1-系统配置, 0-无缓存, >0:缓存
    def rhtml(self, url, scet='', cache=-1):
        cfgs = self.cfgs
        if cache<0:
            cache = int(cfgs['cj360']['cacexp'])
        if not cache:
            return urlpy.page(url, scet)
        fp = cfgs['cj360']['cacdir'] + '/pages/' + files.autnm(url, 1)
        ok = files.tmok(fp, cache)
        if ok:
            html = files.get(fp, 'utf-8')
            html = files.get(fp)
        else:
            html = urlpy.page(url, scet)
            files.put(fp, html)
        return html

'''

'''
