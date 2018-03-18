#coding=UTF-8

import sys, os, time, copy, random
sys.path.append("../")

from core import argv, config, dbop, mdo
cfgs = config.init()

from _exts import cjfang
from multiprocessing import Pool, Process


cdb = dict(copy.deepcopy(cfgs['cdb']), **cfgs['cjdb'])
db = dbop.dbm(cdb)

# 采集单位(批次)
def caiji(name, act):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    
    #time.sleep(random.random() * 3)
    res = cjfang.area(db, act)
    print(res)

    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))

if __name__=='__main__':


    mp = mdo.Pools(3);
    print('\n\n')
    mp.start('p1')

'''
    act = argv.cmd(1)
    print(act)

    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(5):
        p.apply_async(caiji, args=(i,act))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''

