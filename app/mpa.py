#coding=UTF-8

import sys, os
sys.path.append("../")
sys.path.append("./views")

from core import argv, dbop, mdo
from _exts import cjfang

#cdb = dict(copy.deepcopy(cfgs['cdb']), **cfgs['cjdb'])
#db = dbop.dbm(cdb)

if __name__=='__main__':

    # cjfang.area(self.db, act)
    #db = dbop.edb('cjdb'); 
    mp = mdo.Pools(cjfang.area, 'cjdb'); # cjfang.area, db
    mp.start('test', 3)
