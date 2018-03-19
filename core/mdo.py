#coding=UTF-8

import sys, os, time, random
from core import argv, dbop
from multiprocessing import Process, Pool

class Pools:

    def __init__(self, func, param={}):
        self.func = func
        self.param = param # self.setp(param), self.dbk = dbk
        # cannot serialize '_io.BufferedReader' object

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
    def psub(self, no):
        print('Run psub %s (%s)...' % (no, os.getpid()))
        #db = dbop.edb('cjdb') # if self.dbk else dbop.dbm()
        param = self.setp(self.param)
        #param = (db, 'test')
        res = self.func(*param)
        #print(res)
        return res

    def start(self, act='', pcnt=4):
        print('\nParent process %s.' % os.getpid())
        p = Pool(pcnt)
        res = {}
        for i in range(pcnt):
            res = p.apply_async(self.psub, args=('p:'+str(i),))
        print('Waiting for all Pools('+str(pcnt)+') done...')
        p.close()
        p.join()
        print('All Pools done.\n   === res: === \n')
        print(res.get())

'''
        res = {}
        for i in range(self.pcnt):
            func = psubs[key]
            p = Process(target=func, args=(key+':'+str(i),))
            p.start()
        print('Waiting for all Pools('+str(self.pcnt)+') done...')
        print('All Pools done.')
        print(res)
'''
