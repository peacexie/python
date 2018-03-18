#coding=UTF-8

import sys, os, time, random
from multiprocessing import Process, Pool

class Pools:

    def task_tx(self, no):
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        info = 'Task %s runs %0.2f seconds.' % (no, (end-start))
        res = " run "+str(no)+" OK! "
        return [info, res]

    def __init__(self, pcnt=4):
        #self.func = _exts.cjfang
        self.pcnt = pcnt

    # 子进程要执行的代码
    def psub2(self, no):
        print('Run psub2 %s (%s)...' % (no, os.getpid()))
        res = self.task_tx(no)
        print(res[0])
        return res[1]

    # 子进程要执行的代码
    def psub1(self, no):
        print('Run psub1 %s (%s)...' % (no, os.getpid()))
        res = self.task_tx(no)
        print(res[0])
        return res[1]

    def start(self, key):
        psubs = {
            'p1':self.psub1, 
            'p2':self.psub2,
        }
        print('Parent process %s.' % os.getpid())

        p = Pool()
        res = {}
        for i in range(self.pcnt):
            res = p.apply_async(self.psub2, args=(key+':'+str(i),))
            #res = p.apply_async(self.func, args=(key+':'+str(i),))
        print('Waiting for all Pools('+str(self.pcnt)+') done...')
        p.close()
        p.join()
        print('All Pools done.')
        print('res:'); print(res.get())

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
if __name__=='__main__':
    mp = Pools(3);
    print('\n\n')
    mp.start('p1')
    print('\n\n')
    mp.start('p2')
'''