
import sys, os, time, copy, random
from multiprocessing import Process

class prec1:

    # 子进程要执行的代码
    def psub(self, no):
        print('Run task %s (%s)...' % (no, os.getpid()))
        start = time.time()
        time.sleep(random.random() * 3)
        end = time.time()
        print('Task %s runs %0.2f seconds.' % (no, (end-start)))

    def pmain(self, flag):
        print(flag)
        print('Parent process %s.' % os.getpid())
        print('for-:Start')
        for i in range(0,5):
            p = Process(target=self.psub, args=('test:'+str(i),))
            p.start()
            #p.join()
        print('for-:End.')

if __name__=='__main__':
    mt1 = prec1();
    mt1.pmain('xxx')
