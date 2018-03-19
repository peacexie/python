#coding=UTF-8

import sys, os
sys.path.append("../")
sys.path.append("./views")

from core import argv, mdo

if __name__=='__main__':

    # > mpa.py url test/done
    mkey = 'caiji'
    part = argv.cmd(1)
    act = argv.cmd(1)

    mp = mdo.Pools(mkey);
    mp.start(part, act)
