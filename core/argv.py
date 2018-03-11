
import sys, os
from flask import request as freq, g

def cmd(no): #no:1,2,3
    args = sys.argv
    val = args[no] if len(args)>no else ''
    return val

def get(key, d=''):
    val = freq.args.get(key)
    if not val or len(val)==0:
        val = d
    return val
