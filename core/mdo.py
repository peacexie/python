#coding=UTF-8 # 这个文件不该放在core里面
# 鸡肋啦... 大批量采集容易封ip, 出错调试也易出问题

import sys, os, time, random
from core import argv, dbop
from _exts import cjfang
from multiprocessing import Process, Pool

# 计算批次,给多进程使用
def ranb(pcnt, no, cmax, cmin):
    cbat = int(cmax / pcnt)
    n1 = (no*cbat) + cmin
    n2 = cmax if pcnt==no+1 else ((no*cbat)+cbat)
    if n2>cmax:
        n2 = cmax
    res = {'n1':n1, 'n2':n2}
    #print(res)
    return res
# 计算批次,给多进程使用
def limb(pcnt, no, recs):
    cbat = int(recs / pcnt)
    if not no:
        limit = "LIMIT " + str(cbat)
    elif pcnt==no+1:
        limit = "LIMIT " + str(no*cbat) + ',9912399'
    else:
        limit = "LIMIT " + str(no*cbat) + ',' + str(cbat)
    #print(limit)
    return limit

class Pools:

    def __init__(self, mkey, dbk=''):
        self.mkey = mkey
        #self.dbk = dbk
        #self.func = cjfang.area
        self.pcnt = 2

    def setp(self, param={}):
        params = []
        for key in param:
            val = param[key]
            if key=='db':
                val = dbop.edb(val) if val else dbop.dbm()
            params.append(val)
        return tuple(params)
        pass

    # 子进程要执行的代码
    def dosub(self, act, no):
        print('Run psub %s (%s)...' % (no, os.getpid()))
        #param = self.setp(self.param)
        #res = self.func(*param)
        res = {'msg':'Doing sth. in dosub'}
        return res

    # 子进程采集
    def caiji(self, part, act, no):
        print('Run caiji : part=%s, no=%s, pid=(%s)...' % (part, no, os.getpid()))
        cmin = int(cjfang.cfg('pagemin'))
        cmax = int(cjfang.cfg('pagemax'))
        #cbat = int(cjfang.cfg('delimit'))
        db = dbop.edb('cjdb')
        tab = 'img' if part=='save' else 'url'
        itmc = db.get("SELECT COUNT(*) AS cnt FROM {"+tab+"}")
        recs = itmc[0]['cnt']
        limit = limb(self.pcnt, no, recs)
        res = {}
        if part=='url':
            rng = ranb(self.pcnt, no, cmax, cmin)
            n1 = rng['n1']; n2 = rng['n2'];
            for i in range(n1, n2+1):
                re = cjfang.urlp(db, act, i)
            res = rng
        elif part=='data':
            itms = db.get("SELECT * FROM {url} WHERE f1=0 ORDER BY id "+limit)
            for row in itms:
                re = cjfang.datap(db, act, row)
            res = {'limit':limit}
        elif part=='img': # ???
            itms = db.get("SELECT * FROM {url} WHERE f2=0 ORDER BY id "+limit)
            for row in itms:
                re = cjfang.imgp(db, act, row)
            res = {'limit':limit}
        elif part=='save':
            itms = db.get("SELECT * FROM {img} WHERE f1=0 ORDER BY id "+limit)
            for row in itms:
                re = cjfang.imgs(db, act, row)
            res = {'limit':limit}
            pass
        else:
            res = cjfang.area(db, act)
        return res

    def start(self, part, act, pcnt=4):
        self.pcnt = pcnt
        print('\nParent process %s.' % os.getpid())
        dofunc = self.getfunc(); 
        p = Pool(pcnt)
        res = {}
        for i in range(pcnt):
            res = p.apply_async(dofunc, args=(part, act, i))
        print('Waiting for all Pools('+str(pcnt)+') done...')
        p.close()
        p.join()
        print('All Pools done.\n   === res: === \n')
        print(res.get())

    def getfunc(self):
        mtab = {
            'caiji':self.caiji,
            # dosub for test 
            'dosub':self.dosub
        }
        return mtab[self.mkey]


'''

'''
