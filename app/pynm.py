#coding=UTF-8

import sys, os
sys.path.append("./")
sys.path.append("../")
from libs import mpnews

if __name__=='__main__':

    # eg. > mpa.py
    # parts分组: 手动设置, 若8核cpu,设置4-6个分组

    parts = [
        ['all'],
        ['dg'],
        ['gz'],
        ['sz'],
        ['hz','zs','zh']
    ]
    pcnt = len(parts)
    act = '0'

    mp = mpnews.Pools('cjtab1'); # cjtab1,dosub
    mp.start(parts, act, int(pcnt))
