#coding=UTF-8

import copy, re, time
from core import argv, dbop, files, urlpy
from urllib import parse
from pyquery import PyQuery as pyq
from libs import cjtool

'''
0-默认,
1-爬网址,2-已过滤,3/7-爬内容,4-爬图片,5-预留
7-爬内容/待入库
8-已入库,9-已删除
'''

class main:

    # 构造/析构
    def __init__(self):
        self.cfgs = argv.init('1')
        self.db = dbop.dbm(self.cfgs['cdb'])
    def __del__(self):
        #print('-cjnews:end-')
        self.db.close(); 

    # 保存一笔详情数据
    def saveDetail(self, rule, rowb, istest=0):
        kid = str(rowb['id'])
        rowd = self.getDetail(rule, rowb['url'])
        frem = cjtool.skips(rule, rowb, rowd)
        flag = '2' if len(frem)>0 else '7';
        ftab = 'flag=%s,frem=%s,ctime=%s, detail=%s,dpub=%s,dfrom=%s, '
        ftab += 'catid=%s,sfrom=%s,suser=%s'
        ctime = time.strftime("%m-%d %H:%M", time.localtime())
        sqli = "UPDATE {crawl_data} SET "+ftab+" WHERE id=%s"
        rowi = (flag,frem,ctime, rowd['detail'],rowd['dpub'],rowd['dfrom'], 
            rule['catid'],rule['sfrom'],rule['suser'], kid)
        if not istest:
            res = self.db.exe(sqli,rowi)
        else:
            dt = rowd['detail']
            rowd['detail'] = dt[0:240] +' ...... '+ dt[-120:]
            print(rowd)
        if not frem:
            frem = 'update-ok'
        return 'data-'+kid+' : ' + frem
    # 取出未采集详情的列表
    def getDList(self, part, istest=0):
        if not part or part=='0':
            whr = '';
        elif part.isdigit():
            whr = " AND id='"+part+"'";
        else:
            whr = " AND city='"+part+"'"
        wtest = "1=1" if istest else "flag=1"
        sql = "SELECT * FROM {crawl_data} WHERE "+wtest+whr
        lists = self.db.get(sql,())
        return lists;

    # 获取规则 part:{city,name,rid,did,act}
    def getRules(self, part, act, istest=0):
        # dict.get(key, default=None)
        whr = ''; pms = ()
        if act=='dict':
            if part['city']:
                whr += " AND city=%s"
                pms += (part['city'],)
            if part['name']:
                whr += " AND name LIKE %s"
                pms += ('%'+part['name']+'%',)
            if part['rid']:
                whr += " AND id=%s"
                pms += (part['rid'],)
            topn = 3
        else:
            if not part or part=='0':
                whr = '';
                pms += ()
            elif part.isdigit():
                rid = part
                if act=='cont' and part.isdigit(): # 找出当前内容的 ruleid ??? 
                    sql = "SELECT * FROM {crawl_data} WHERE id="+rid
                    row = self.db.get(sql,(),1)
                    rid = str(row['ruleid']) if row else '0'
                whr = " AND id=%s";
                pms += (parts['rid'],)
            else:
                whr += " AND city=%s"
                pms += (part,)
            topn = None
        wtest = "1=1" if istest else "status=1"
        sql = "SELECT * FROM {crawl_rule} WHERE "+wtest+whr
        rules = self.db.get(sql,pms,topn)
        return rules;
    # 爬1个规则的列表
    def pyUrls(self, rule, istest=0):
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
                if not istest:
                    rs = self.db.exe(sqli,rowi)
                res[no] = 'insert : '+url
            else: # print('skip')
                res[no] = 'skip : '+url
            no += 1;
        return res

    # 采集-获取Url列表
    def getUList(self, rule={}):
        html = self.rhtml(rule['url'])
        html = cjtool.htmDeel(rule, html, 'pre_list')
        doc = pyq(html)
        itms = []
        lists = doc(rule['slist'])
        for li in lists:
            attu = 'href' if rule['surl']=='a' else 'text'
            url = cjtool.pqv(li, rule['surl'], attu)
            title = cjtool.pqv(li, rule['stitle'], 'text')
            if not url or not title:
                continue
            ug = re.search('pre_url=='+'([^\n|\r])+', rule['cfgs']) #, re.I
            if ug:
                rp = ug.span() #;print(rp)
                ubase = rule['cfgs'][rp[0]+9:rp[1]]
                url = ubase + url
            else:
                url = urlpy.fxurl(url, rule['url'])
            itms.append({'url':url, 'title':title})
        #print(itms[0])
        return itms;
    # 采集-获取详情
    def getDetail(self, rule={}, url=''):
        res = {'errno':1, 'errmsg':''}
        html = self.rhtml(url)
        html = cjtool.htmDeel(rule, html, 'pre_cont')
        doc = pyq(html)
        detail = cjtool.pqv(doc, rule['detail'], 'html')
        detail = cjtool.repCont(rule['cfgs'], 'tab_repd', detail)
        detail = cjtool.repImgs(url, detail)
        dpub = cjtool.pqv(doc, rule['dpub'], 'text')
        dpub = cjtool.repCont(rule['cfgs'], 'tab_rept', dpub)
        dfrom = cjtool.pqv(doc, rule['dfrom'], 'text')
        return {'dpub':dpub, 'dfrom':dfrom, 'detail':detail}

    # cache: 1-系统配置, 0-无缓存, >0:缓存
    def rhtml(self, url, scet='', cache=-1):
        cfgs = self.cfgs
        if cache<0:
            cache = int(cfgs['ucfg']['cacexp'])
        if not cache:
            return urlpy.page(url, scet)
        fp = cfgs['dir']['cache'] + '/pages/' + files.autnm(url, 1)
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
