
import sys, os, time, copy, random
from multiprocessing import Process

# 子进程要执行的代码
def run_proc(no):
    print('Run task %s (%s)...' % (no, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (no, (end-start)))

if __name__=='__main__':

    print('Parent process %s.' % os.getpid())
    for i in range(0,5):
        p = Process(target=run_proc, args=('test:'+str(i),))
        p.start()
        #p.join()
    print('Process will start.')

    print('Process end.')