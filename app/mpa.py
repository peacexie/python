#coding=UTF-8

import sys, os
sys.path.append(sys.path[0])
sys.path.append(sys.path[0] + "/../")
from core import argv
argv.init() # libs需要先.init()
from libs import mdo

if __name__=='__main__':

    # > mpa.py url test/done
    part = argv.cmd(1)
    act = argv.cmd(2)
    pcnt = argv.cmd(3, 2)

    mp = mdo.Pools('caiji'); # caiji,dosub
    mp.start(part, act, int(pcnt))
