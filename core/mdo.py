#coding=UTF-8

import sys, os, time, random
from core import argv, dbop
from _exts import cjfang
from multiprocessing import Process, Pool

class Pools:

    def __init__(self, mkey, dbk=''):
        self.mkey = mkey
        #self.dbk = dbk
        #self.func = cjfang.area

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
    def caiji(self, act, no):
        print('Run caiji : act=%s, no=%s, pid=(%s)...' % (act, no, os.getpid()))
        db = dbop.edb('cjdb')
        #param = self.setp(self.param)
        # urlp,datap,imgp,imgs,area
        param = (db, 'test', 4)
        res = cjfang.urlp(*param)
        return res

    def start(self, part, act, pcnt=4):
        print('\nParent process %s.' % os.getpid())
        dofunc = self.getfunc(); 
        p = Pool(pcnt)
        res = {}
        for i in range(pcnt):
            res = p.apply_async(dofunc, args=(act, i))
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
