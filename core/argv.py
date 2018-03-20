
import sys, os
from flask import request as freq
global cfgs

# 得到命令行参数, no=1,2,3
def cmd(no, d=''):
    args = sys.argv
    val = args[no] if len(args)>no else d
    return val

# 得到Url参数, d:默认值
def get(key, d=''):
    val = freq.args.get(key)
    if not val or len(val)==0:
        val = d
    return val

# cfgs:运行时参数:取值/赋值
def cfg(key, val=None):
    global cfgs
    if val is None:
        return cfgs[key] if hasattr(cfgs, key) else None
        pass #get
    else:
        cfgs[key] = val
        pass #get
