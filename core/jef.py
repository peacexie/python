
import os, sys, time
from flask import g
from core import dbop

# fef=jinja_env.filters=jinja过滤器

# 生成url, 不如直接这样写: mod-key?parms 或 ../group/mod-key?parms
# {{ 'home-index' | url('a=b') }}, 无多大意义?
def url(mkv, p=''):
    if mkv=='/':
        mkv = '/root/'
    elif mkv=='./':
        mkv = '/' + g.mkvs['group'] + '/'
    elif mkv.find('/')<0: # mkv
        mkv = '/' + g.mkvs['group'] + '/' + mkv
    #else: # /gid/mkv 
    #    mkv = mkv
    mkv = mkv.replace('/root/', '/')
    return mkv + ('?'+p  if len(p)>0 else '')

# 运行调试信息
# {{ ''|info }}
def info(p=''):
    timer = time.time()-g.run['timer']
    tfull = g.mkvs['group'] + '/' + g.mkvs['tpname'];
    tupd = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msg = 'run:' + str(round(timer,3)) + '(s), tpl:' + tfull + ', upd:' + tupd
    return msg
    # Done:37.102/149.760(ms); 13(queries)/1.178(MB); Tpl:c_page/_home; Upd:2018-03-02 17:59:30

# 获取db资料
# {% set arcs1 = g.db.get("SELECT * FROM {article}",(),1) %}
def get(sql, parms=(), re=None):
    return g.db.get(sql, parms, re)

# 执行sql执行sql语句
def exe(sql, parms=(), mod=None):
    return g.db.exe(sql, parms, mod)
