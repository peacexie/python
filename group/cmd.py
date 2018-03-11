#coding=UTF-8

import sys, os, time, copy, random
from multiprocessing import Pool

def task_t1(name):
    print( 'Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print( 'Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    # test
    args = sys.argv
    print(args[1])

    print( 'Parent process %s.' % os.getpid())
    p = Pool()
    # for i in range(0, 10, 3)
    for i in range(5):
        p.apply_async(task_t1, args=(i,))
    print( 'Waiting for all subprocesses done...')
    p.close()
    p.join()
    print( 'All subprocesses done.')
