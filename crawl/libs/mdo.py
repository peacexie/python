#coding=UTF-8 # 这个文件不该放在core里面
# 鸡肋啦... 大批量采集容易封ip, 出错调试也易出问题

import sys, os, time, random
from core import argv, dbop
from libs import cjnews, cjtool, cjfang
from multiprocessing import Process, Pool

class Pools:

    def __init__(self, mkey, dbk=''):
        self.mkey = mkey
        #self.dbk = dbk
        #self.func = cjfang.area
        #self.cj = cjnews.main()
        self.pcnt = 2
    def __del__(self):
        print('-Pools:end-')
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
        cj = cjnews.main()
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
        limit = argv.limit(self.pcnt, no, recs)
        res = {}
        if part=='url':
            rng = argv.range(self.pcnt, no, cmax, cmin)
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
        #self.cj.db.close(); 
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
