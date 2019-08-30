#coding=UTF-8 # 这个文件不该放在core里面
# 鸡肋啦... 大批量采集容易封ip, 出错调试也易出问题

import sys, os, json, time, random
from core import argv, files, dbop
from libs import cjnews, cjtool
from multiprocessing import Process, Pool

class Pools:

    def __init__(self, mkey, dbk=''):
        self.mkey = mkey
        self.pcnt = 2
    def __del__(self):
        return
        #print("\n -Pools:end-")
        #self.db.close(); 

    def setp(self, param={}):
        params = []
        for key in param:
            val = param[key]
            if key=='db':
                val = dbop.edb(val) if val else dbop.dbm()
            params.append(val)
        return tuple(params)

    # 子进程要执行的代码
    def dosub(self, part, act, no):
        print('Run psub %s (%s)...' % (no, os.getpid()))
        #param = self.setp(self.param)
        #res = self.func(*param)
        #cj = cjnews.main()
        res = {'msg':'Doing sth. in dosub'}
        return res

    # 子进程-一组城市
    def cjtab1(self, ctab1, act, no):
        print('Run cjtab1 : ctab1=%s, no=%s, pid=(%s)...' % (ctab1, no, os.getpid()))
        resm = {}
        for i in range(len(ctab1)):
            try:
                city = ctab1[i]
                resm[i] = self.cjcity(ctab1[i], act, no)
            except Exception as ex:
                resm[i] = ex
        stamp = time.strftime("%Y%m%d-%H%M%S", time.localtime())
        cfgs = argv.init('1')
        fp = stamp +'-'+ '+'.join(ctab1) +'.txt'
        data = json.dumps(resm, indent=4, separators=(',',': '), ensure_ascii=True)
        # sort_keys=True,indent=4, separators=(',',': '), ensure_ascii=True
        files.put(cfgs['dir']['cache']+'/debug/'+fp, data)
        return resm;

    # 子进程-一个城市
    def cjcity(self, city, act, no):
        debug = cjtool.debug()    
        # 得到规则
        cj = cjnews.main()
        rules = cj.getRules(city, act, 0)
        if not rules:
            return {'errno':'1001', 'errmsg':'规则为空',}
        # 爬连接
        for rule in rules:
            res = cj.pyUrls(rule)
            debug['link'][rule['id']] = res
        # 按下标整理规则字典
        rdic = {}
        for rule in rules:
            rdic[rule['id']] = rule
        # 取出未采集详情的列表
        lists = cj.getDList(city)
        for itm in lists:
            if not itm['ruleid'] in rdic.keys():
                continue
            rule = rdic[itm['ruleid']];
            res = cj.saveDetail(rule, itm)
            debug['cont'][itm['id']] = res
        return {'errno':'0', 'debug':debug}

    def start(self, parts, act, pcnt=4):
        self.pcnt = pcnt
        print('\nParent process %s.' % os.getpid())
        dofunc = self.getfunc(); 
        p = Pool(pcnt)
        res = {}
        for i in range(len(parts)):
            ctab1 = parts[i]; k = int(1%2)
            #res = self.cjtab1(ctab1, act, i)
            res = p.apply_async(dofunc, args=(ctab1, act, i))
        print('Waiting for all Pools('+str(pcnt)+') done...')
        p.close()
        p.join()
        print('All Pools done.\n   === res: === \n')
        #print(res.get())

    def getfunc(self):
        mtab = {
            'cjtab1':self.cjtab1,
            # dosub for test 
            'dosub':self.dosub
        }
        return mtab[self.mkey]

