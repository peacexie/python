#coding=UTF-8

import sys, os
sys.path.append("./")
sys.path.append("../")
from libs import mdo

if __name__=='__main__':

    # > mpa.py
    parts = [ # 手动设置分组
        ['dg'],
        ['gz'],
        ['sz'],
        ['hz','zs','zh']
    ]
    pcnt = len(parts)
    act = '0'

    mp = mdo.Pools('cjtab1'); # cjtab1,dosub
    mp.start(parts, act, int(pcnt))
