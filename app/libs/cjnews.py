#coding=UTF-8

import copy, re, time
from core import argv, dbop, files, urlpy
from urllib import parse
from pyquery import PyQuery as pyq
from libs import cjtool, proxys

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
        return
        #print('-cjnews:end-')
        #self.db.close(); 

    # 保存一笔详情数据
    def saveDetail(self, rule, rowb, istest=0):
        kid = str(rowb['id'])
        rowd = self.getDetail(rule, rowb['url'])
        frem = cjtool.skips(rule, rowb, rowd)
        flag = '2' if len(frem)>0 else '7';
        ftab = 'flag=%s,frem=%s,ctime=%s, detail=%s,dpub=%s,dfrom=%s, '
        ftab += 'catid=%s,sfrom=%s,suser=%s'
        ctime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
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
    def getDList(self, part, act='', istest=0):
        if not part or part=='0':
            whr = '';
        elif part.isdigit():
            fid = "id" if act=='rowc' else "ruleid"
            whr = " AND "+fid+"='"+part+"'";
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
            topn = 30
        else:
            if not part or part=='0':
                whr = '';
                pms += ()
            elif part.isdigit():
                rid = part  
                if act=='rowc': # 找出当前内容的 ruleid ??? 
                    sql = "SELECT * FROM {crawl_data} WHERE id="+rid
                    row = self.db.get(sql,(),1)
                    rid = str(row['ruleid']) if row else '0'
                whr = " AND id=%s";
                pms += (rid,)
            else:
                whr += " AND city=%s"
                pms += (part,)
            topn = None
        wtest = "1=1" if istest else "status=1"
        sql = "SELECT * FROM {crawl_rule} WHERE "+wtest+whr+" ORDER BY id DESC"
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
                fields = 'city,flag,ruleid,title,url,list_ext1,list_ext2,list_ext3'
                sqli = "INSERT INTO {crawl_data} ("+fields+")VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                ex = rb['exts'] ;print(ex)
                rowi = (rule['city'],'1',rule['id'],rb['title'],rb['url'],ex['ext1'],ex['ext2'],ex['ext3'])
                if not istest:
                    rs = self.db.exe(sqli,rowi)
                res[no] = 'insert : '+url
            else: # print('skip')
                res[no] = 'skip : '+url
            no += 1;
        return res

    # 采集-获取Url列表
    def getUList(self, rule={}):
        html = self.rhtml(rule['url'], rule['agent'])
        html = cjtool.htmDeel(rule, html, 'pre_list')
        itms = []
        if isinstance(html, list):
            if len(html)>0:
                for i in range(len(html)):
                    row = html[i]
                    itms.append({'url':row[rule['surl']], 'title':row[rule['stitle']]})
            return itms
        doc = pyq(html)
        lists = doc(rule['slist'])
        for li in lists:
            if not rule['surl']:
                url = pyq(li).attr('href')
            else:
                atu = 'href' if (rule['surl']=='a' or ' a' in rule['surl']) else 'text';
                url = cjtool.pqv(li, rule['surl'], atu)
            if not rule['stitle']:
                title = pyq(li).text()
            else:
                title = cjtool.pqv(li, rule['stitle'], 'text')
            #print(' aaa: ', url, title)
            if (not url) or (not title):
                continue
            ug = re.search('pre_url=='+'([^\n|\r])+', rule['cfgs']) #, re.I
            if ug and (not '://' in url):
                rp = ug.span() #;print(rp)
                ubase = rule['cfgs'][rp[0]+9:rp[1]]
                url = ubase + url
            else:
                url = urlpy.fxurl(url, rule['url'])
            exts = {}
            for i in range(1,4):
                exts['ext'+str(i)] = ''
                if rule['list_ext'+str(i)]:
                    exts['ext'+str(i)] = cjtool.pqv(li, rule['list_ext'+str(i)], 'text')
            # >255 的资料，应该是出错，不要的，这里保存供后续调试分析
            url = url if len(url)<254 else url[0:254]
            title = title if len(title)<254 else title[0:254]
            itms.append({'url':url, 'title':title, 'exts':exts})
        #print(itms[0])
        return itms;
    # 采集-获取详情
    def getDetail(self, rule={}, url=''):
        res = {'errno':1, 'errmsg':''}
        html = self.rhtml(url, rule['agent'])
        html = cjtool.htmDeel(rule, html, 'pre_cont')
        doc = pyq(html)
        detail = cjtool.pqv(doc, rule['detail'], 'html')
        detail = cjtool.repCont(rule['cfgs'], 'tab_repd', detail)
        detail = cjtool.repImgs(url, detail)
        #reg = r'\<script[^>]*\>(.*)\<\/script\>'
        reg = re.compile(r"<script.*?</script>", re.S|re.I)
        detail = re.sub(reg, '', detail)
        dpub = cjtool.pqv(doc, rule['dpub'], 'text')
        dpub = cjtool.repCont(rule['cfgs'], 'tab_rept', dpub)
        dfrom = cjtool.pqv(doc, rule['dfrom'], 'text')
        return {'dpub':dpub, 'dfrom':dfrom, 'detail':detail}

    # cache: 1-系统配置, 0-无缓存, >0:缓存
    def rhtml(self, url, agent=0, cache=-1):
        cfgs = self.cfgs
        if cache<0:
            cache = int(cfgs['ucfg']['cacexp'])
        if not cache:
            return self.rdata(url, agent)
        fp = cfgs['dir']['cache'] + '/pages/' + files.autnm(url, 1)
        ok = files.tmok(fp, cache)
        if ok:
            html = files.get(fp, 'utf-8')
            html = files.get(fp)
        else:
            html = self.rdata(url, agent)
            files.put(fp, html)
        return html

    def rdata(self, url, agent=0):
        uag = proxys.getAgent()
        uip = {} #proxys.getProxy() if agent else {}
        data = urlpy.page(url, {'User-Agent':uag}, uip)
        return data

'''

'''
