# -*- coding:UTF-8 -*-

import sys, os, json
from core import argv, files, parse
from flask import g

# 格式化输出(xml,json[p])
def vmft(d):
    if d['tpname']=='xml':
        xml = parse.convXml.collectionToXML(d)
        res = parse.convXml.getXmlString(xml)
    else:
        res = json.dumps(d, ensure_ascii=False)
        cb = argv.args.get('callback')
        if cb:
            res = cb + '(' + res + ');'
    ctype = {'Content-Type':vtyp(d['tpname'])}
    return res, d['code'], ctype

# 读取: root: /robots.txt, favicon.ico 等
def vrfp(fp):
    data = files.get('./static/root/doc/'+fp, '') # g.dri['static'] ??? 
    code = 200 if len(data)>0 else 404
    exts = os.path.splitext(fp)
    ctype = {'Content-Type':vtyp(exts[1])}
    return data, code, ctype

# 错误处理,
def verr(d):
    # null-tpl
    if len(d['tpname'])==0:
        d['code'] = 404
        d['message'] = '[' + d['tpath'] + '/' + d['tpdef'] + '] Template NOT Found!'
    # home-error
    if d['group']=='root' and g.mkvs['mkv']=='home-error':
        d['code'] = 403
        d['message'] = '[/error] HTTP 403 Forbidden!'
    # 40x-tpl
    if d['code']>=400:
        if g.sys['debug']=='False':
            abort(d['code'], d['message'])
        d['full'] = 'root' + '/' + 'home/error' + g.dir['tpext']
    else:
        d['full'] = d['group'] + '/' + d['tpname'] + g.dir['tpext']
    g.run['full'] = d['full']
    # 40x-def-url
    if d['tpname']=='dir' and d['message']=='':
        d['message'] = '/'
    #return d 

# mete类型
def vtyp(ext):
    ext = ext.replace('.', '')
    dic = {
        'ico':'image/x-icon',
        'txt':'text/plain',
        'htm':'text/html',
    } # jpg,jpeg,gif
    if ext in dic.keys():
        ctype = dic[ext]
    else:
        ctype = 'application/'+ext+''
    if '(,txt,htm,html,json,jsonp,xml)'.find(','+ext+',')>0:
        ctype = ctype+';charset=utf-8'
    return ctype
