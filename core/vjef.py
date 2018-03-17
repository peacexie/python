
import sys, os, time, random
from core import dbop
from flask import g

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
def info(p='', n=2):
    timer = time.time()-g.run['timer']
    stim = 'run:' + str(round(timer,3)) + '(s)'
    stpl = 'tpl:' + g.run['full'] #g.mkvs['group'] + '/' + g.mkvs['tpname'];
    supd = 'upd:' + time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if len(p)>0:
        if n==1:
            stim = "<a href='"+p+"'>"+stim+"</a>"
        if n==2:
            stpl = "<a href='"+p+"'>"+stpl+"</a>"
        if n==3:
            supd = "<a href='"+p+"'>"+supd+"</a>"
    msg = stim + ', ' + stpl + ', ' + supd
    return msg

'''
def rnd(p=''):
    return time.time() #g.run['timer'] random.random() #time.time()
'''

# 获取db资料
# {% set arcs1 = g.db.get("SELECT * FROM {article}",(),1) %}
def get(sql, parms=(), re=None):
    return g.db.get(sql, parms, re)

# 执行sql执行sql语句
def exe(sql, parms=(), mod=None):
    return g.db.exe(sql, parms, mod)
