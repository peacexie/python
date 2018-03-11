

import sys, os, time, copy, random
from multiprocessing import Pool

class myPool:

    def task_t2(self, mod='dm', act='da'):
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print(' \ntask_t2 task_t2 ============\n ')
        print(mod)
        print(act)
        res = 'Task %s runs %0.2f seconds.' % (no, (end-start))
        print(res)
        return res

    def __init__(self, func=None, pcnt=4, args=()):
        self.func = func
        self.pcnt = pcnt
        self.args = args

    # 子进程要执行的代码
    def psub(self, no):
        print('Run task %s (%s)...' % (no, os.getpid()))
        res = self.task_t2('xxx')
        print(res)
        return res

    def start(self, flag):
        print('Parent process %s.' % os.getpid())
        p = Pool()
        rep = {}
        for i in range(5):
            rep['res:'+str(i)] = p.apply_async(self.psub, args=('test:'+str(i),))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
        print(rep)

if __name__=='__main__':
    mp = myPool(3, ('mymod','myact'));
    mp.start('xxx')
