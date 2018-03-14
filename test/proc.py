

import os, time, copy, random
from multiprocessing import Pool

#cdb = dict(copy.deepcopy(g.cdb), **g.cjdb)
#db = dbop.dbm(cdb)
#res = cjfang.urlp(db, act, i)

def long_time_task(name):
    print( 'Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print( 'Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print( 'Parent process %s.' % os.getpid())
    p = Pool()
    # for i in range(0, 10, 3)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print( 'Waiting for all subprocesses done...')
    p.close()
    p.join()
    print( 'All subprocesses done.')
