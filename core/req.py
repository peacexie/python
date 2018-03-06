
from flask import request, g

def get(key, d=''):
    val = request.args.get(key)
    if not val or len(val)==0:
        val = d
    return val
