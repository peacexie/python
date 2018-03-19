#coding=UTF-8

import sys, os
sys.path.append("../")
sys.path.append("./views")

from core import argv, mdo
from _exts import cjfang

if __name__=='__main__':

    # cjfang.area(self.db, act, min, max)
    #db = dbop.edb('cjdb'); 
    param = {'db':'cjdb', 'act':'test', 'min':'3', 'max':'5',} #(db, 'test')
    mp = mdo.Pools(cjfang.area, param); # cjfang.area, db
    mp.start('test', 3)
