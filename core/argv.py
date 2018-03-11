
from flask import request as freq, g

def get(key, d=''):
    val = freq.args.get(key)
    if not val or len(val)==0:
        val = d
    return val
