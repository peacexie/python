
import sys, os
from flask import request as freq

# 得到命令行参数, no=1,2,3
def cmd(no):
    args = sys.argv
    val = args[no] if len(args)>no else ''
    return val

# 得到Url参数, d:默认值
def get(key, d=''):
    val = freq.args.get(key)
    if not val or len(val)==0:
        val = d
    return val

# run:运行时参数:取值/赋值
def xxx_rt(tmp, key, val=None):
    global run
    if val is None:
        pass #set
    else:
        pass #get

