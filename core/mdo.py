#coding=UTF-8

import sys, os, time, random
from core import argv, dbop
from multiprocessing import Process, Pool

class Pools:

    def execute(self, *args):
        #print(args)
        #print(self.name)
        res = getattr(self, self.func)(*args)

    def task_tx(self, no):
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        info = 'Task %s runs %0.2f seconds.' % (no, (end-start))
        res = " run "+str(no)+" OK! "
        return [info, res]

    def __init__(self, func, dbk=''):
        self.func = func
        self.dbk = dbk # cannot serialize '_io.BufferedReader' object
        pass

    # 子进程要执行的代码
    def psub(self, no):
        print('Run psub1 %s (%s)...' % (no, os.getpid()))
        #res = self.task_tx(no)
        db = dbop.edb(self.dbk) if self.dbk else dbop.dbm()
        param = (db, 'test')
        res = self.func(*param)
        #res = apply(self.func, (db,'test')) 
        #print(res)
        return res

    def start(self, act='', pcnt=4):

        print('Parent process %s.' % os.getpid())

        p = Pool(pcnt)
        res = {}
        for i in range(pcnt):
            res = p.apply_async(self.psub, args=('p:'+str(i),))
            #param = (self.db, 'test')
            #res = p.apply_async(self.func, args=param)
        print('Waiting for all Pools('+str(pcnt)+') done...')
        p.close()
        p.join()
        print('All Pools done.')
        print('\nres:\n'); 
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

'''

# 采集单位(批次)
def caiji(name, act):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    
    #time.sleep(random.random() * 3)
    res = cjfang.area(db, act)
    print(res)

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))

'''