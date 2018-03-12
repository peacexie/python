
import sys, os, time, random
from multiprocessing import Pool

class myPool:

    def task_tx(self, no):
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print('task_'+str(no)+' ============')
        res = 'Task %s runs %0.2f seconds.' % (no, (end-start))
        return res

    def __init__(self, pcnt=4):
        self.pcnt = pcnt

    # 子进程要执行的代码
    def psub2(self, no):
        print('Run psub2 %s (%s)...' % (no, os.getpid()))
        res = self.task_tx(no)
        print(res)
        return res

    # 子进程要执行的代码
    def psub1(self, no):
        print('Run psub1 %s (%s)...' % (no, os.getpid()))
        res = self.task_tx(no)
        print(res)
        return res

    def start(self, key):
        psubs = {
            'p1':self.psub1, 
            'p2':self.psub2,
        }
        print('Parent process %s.' % os.getpid())
        p = Pool()
        rep = []
        for i in range(self.pcnt):
            func = psubs[key]
            rep.append(p.apply_async(func, args=('test:'+str(i),)))
            #rep.append(p.apply_async(self.func, args=self.args))
        print('Waiting for all subprocesses done...')
        p.close()
        p.join()
        print('All subprocesses done.')
        for res in rep:
            print(res.get())

'''
if __name__=='__main__':
    mp = myPool(3);
    mp.start('p1')
    mp.start('p2')

'''

